#!/usr/bin/env python3
"""Fail closed on missing context, missing source assets or accidental 'approved' claims.

This is a document-integrity checker; NOT an ERC, DRC, electrical or fabrication test.
"""
from pathlib import Path
import csv, json, re, sys
ROOT=Path(__file__).resolve().parents[1]
REQUIRED=[
 'AGENTS.md','.github/copilot-instructions.md','.vscode/mcp.json',
 'docs/requirements.md','docs/functional-delta-register.csv','docs/test-matrix.csv',
 'docs/safety-gates.md','docs/architecture.md','docs/mcp-setup.md',
 'hardware/rev-c/design-contract.json','hardware/rev-c/target-netmap.csv',
 'hardware/rev-c/BOM_candidates.csv','reference/original/original_schematic.png',
 'reference/original/original_gerbers.zip',
 'reference/rev-b/easyeda_schematic_standard.json',
 'reference/rev-b/easyeda_pcb_standard.json'
]
ERRORS=[]
def check(t,why):
    if not t: ERRORS.append(why)
def csv_rows(rel):
    with (ROOT/rel).open(newline='',encoding='utf-8-sig') as f:return list(csv.DictReader(f))
def main():
    for p in REQUIRED:check((ROOT/p).is_file(),f'Missing required asset: {p}')
    if ERRORS:finish();return 1
    d=json.loads((ROOT/'hardware/rev-c/design-contract.json').read_text(encoding='utf-8'))
    check(d['battery']['cells_series']==1,'Only one series cell permitted')
    check(d['battery']['protection']=='REQUIRED','Battery protection requirement missing')
    check(d['controller']['relay_command_soc_gpio']==3,'Relay GPIO not D1/GPIO3')
    check(d['controller']['relay_command_board_pin']=='D1','Relay command pin not D1')
    if d['fabrication_approved']:
        check(d['maturity']=='RELEASE_REVIEWED', 'Fabrication approval requires release review stage')
        check(d['gates'].get('fabrication_review')=='PASS','Fabrication approval requires manual fabrication review evidence')
    check(d['maturity'] in ['REQUIREMENTS_ONLY','SCHEMATIC_DRAFT','PCB_DRAFT','PROTOTYPE_TESTED','RELEASE_REVIEWED'], 'Unknown maturity stage')
    check(d['controller']['battery_5V_boosted_output_present'] is False,'Unexpected 5V backup claim')
    check(d['battery']['exact_holder_mpn']!='' ,'Unspecified holder MPN must be clearly TBD or verified')
    check(all(v in ['OPEN','FAIL','PASS'] for v in d['gates'].values()),'Unknown gate state')
    for key,status in d['gates'].items():
        if status=='PASS':
            ev=d.get('gate_evidence',{}).get(key,[])
            check(bool(ev) and all((ROOT/f).is_file() for f in ev),f'PASS gate requires committed evidence files: {key}')
    pinset=set(d['interfaces']['breakouts'])
    check(pinset=={f'D{i}' for i in range(2,11)},'GPIO breakout list must preserve D2-D10')
    mcp=json.loads((ROOT/'.vscode/mcp.json').read_text(encoding='utf-8'))
    srv=mcp['servers']['easyeda-mcp-pro']
    check(srv['command']=='npx' and 'easyeda-mcp-pro' in srv['args'],'Wrong MCP command')
    check(srv['env']['TOOL_PROFILE']=='core','Default MCP must start in core profile')
    delta=csv_rows('docs/functional-delta-register.csv')
    must=['STAT_MCP','SWITCH','VBAT_5V','D2-D10','VIN']
    combo=' '.join(str(v) for row in delta for v in row.values())
    for token in must:check(token in combo,f'Missing functional delta: {token}')
    tests=csv_rows('docs/test-matrix.csv')
    check(len(tests)>=10,'Insufficient test scenarios')
    for r in tests:
        check(r['Status'] in ['NOT_RUN','PASS','FAIL'], f'Invalid test status: {r["ID"]}')
        if r['Status']!='NOT_RUN':
            ev=r.get('Evidence','').strip()
            check(bool(ev) and (ROOT/ev).is_file(),f'Executed test requires evidence file: {r["ID"]}')
    check(any('100' in ' '.join(r.values()) for r in tests),'100-cycle switchover test missing')
    # Immutable historical inputs must match their recorded checksums.
    for line in (ROOT/'reference/SHA256SUMS.txt').read_text().splitlines():
        if not line.strip():continue
        expected,rel=line.split('  ',1)
        path=ROOT/rel
        check(path.is_file() and __import__('hashlib').sha256(path.read_bytes()).hexdigest()==expected,f'Altered historical reference: {rel}')
    for name in ('easyeda-mcp-connect','power-path-audit','schematic-rev-c','pcb-layout-dfm','ups-bench-validation','india-bom','fabrication-release'):
        fp=ROOT/'.github/skills'/name/'SKILL.md'
        check(fp.is_file(),f'Missing skill {name}')
        if fp.is_file():
            s=fp.read_text(encoding='utf-8')
            check(s.startswith('---\n') and f'name: {name}' in s,f'Skill frontmatter invalid: {name}')
    for fp in (ROOT/'.github/agents').glob('*.agent.md'):
        check(fp.read_text(encoding='utf-8').startswith('---\n'),f'Agent frontmatter missing: {fp.name}')
    for fp in (ROOT/'.github/prompts').glob('*.prompt.md'):
        check(fp.read_text(encoding='utf-8').startswith('---\n'),f'Prompt frontmatter missing: {fp.name}')
    finish();return 0 if not ERRORS else 1
def finish():
    if ERRORS:
        for err in ERRORS:print('FAIL:',err)
    else:print('PASS: source references, agent context, design constraints and evidence-gated tests consistent (NOT an electrical verification)')
if __name__=='__main__':sys.exit(main())
