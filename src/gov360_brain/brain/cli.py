"""CLI for the active Brain. Read commands never initialize legacy state."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from .catalogue import build, compile_brain, status


def add_parser(subparsers):
    brain = subparsers.add_parser('brain', help='Active Markdown Brain, local context and portable releases')
    brain.add_argument('--root', type=Path, default=Path.cwd())
    commands = brain.add_subparsers(dest='brain_command', required=True)
    commands.add_parser('status')
    commands.add_parser('validate')
    build_parser = commands.add_parser('build')
    build_parser.add_argument('--check', action='store_true')
    context = commands.add_parser('context')
    context.add_argument('query')
    context.add_argument('--domains', nargs='+')
    context.add_argument('--allowed-source-ids', nargs='*')
    context.add_argument('--denied-source-ids', nargs='*')
    context.add_argument('--jurisdiction')
    context.add_argument('--as-of')
    context.add_argument('--token-budget', type=int, default=6000)
    context.add_argument('--require-known-validity', action='store_true',
                         help='exclude citations with unknown temporal/review bounds')
    context.add_argument('--mode', choices=['assistance', 'research'], default='assistance')
    research = commands.add_parser('research', help='Explicit local research in validated ingest; never approved assistance')
    research.add_argument('query')
    research.add_argument('--domains', nargs='+')
    research.add_argument('--allowed-source-ids', nargs='*')
    research.add_argument('--denied-source-ids', nargs='*')
    research.add_argument('--token-budget', type=int, default=6000)
    evaluation = commands.add_parser('evaluate')
    evaluation.add_argument('--suite', choices=['reference', 'extension'], default='reference')
    impact = commands.add_parser('impact', help='Metadata-only dependency impact; no publication')
    selector = impact.add_mutually_exclusive_group(required=True)
    selector.add_argument('--source-id')
    selector.add_argument('--evidence-ref')
    selector.add_argument('--receipt-id')
    export = commands.add_parser('export')
    export.add_argument('--public', action='store_true')
    export.add_argument('--output', type=Path)
    export.add_argument('--check', action='store_true')
    kit = commands.add_parser('release-kit')
    kit.add_argument('--output', type=Path)
    kit.add_argument('--check', action='store_true')
    handoff = commands.add_parser('handoff', help='Build the operator-authorized private CDO continuation snapshot')
    handoff.add_argument('--output', type=Path)
    handoff.add_argument('--check', action='store_true')
    bootstrap = commands.add_parser('bootstrap')
    bootstrap.add_argument('--source-root', type=Path)
    bootstrap.add_argument('--apply', action='store_true')


def dispatch(args) -> dict:
    root = args.root.resolve()
    if args.brain_command == 'status':
        return status(root)
    if args.brain_command == 'validate':
        cat = compile_brain(root)
        errors = [f for f in cat['findings'] if f['severity'] in {'ERROR', 'CRITICAL'}]
        return {**status(root, catalogue=cat), 'valid': not errors, 'errors': errors,
                'warnings': sum(f['severity'] == 'WARNING' for f in cat['findings']),
                'note': 'Technical validity does not establish full evidence coverage.'}
    if args.brain_command == 'build':
        return build(root, write=not args.check)
    if args.brain_command == 'context':
        from .retrieval import build_context
        return build_context(root, args.query, domains=args.domains,
                             allowed_source_ids=args.allowed_source_ids,
                             denied_source_ids=args.denied_source_ids,
                             jurisdiction=args.jurisdiction, as_of=args.as_of,
                             token_budget=args.token_budget, mode=args.mode,
                             require_known_validity=args.require_known_validity)
    if args.brain_command == 'evaluate':
        from .retrieval import evaluate
        return evaluate(root, suite=args.suite)
    if args.brain_command == 'research':
        from .research import research
        return research(root, args.query, domains=args.domains,
                        allowed_source_ids=args.allowed_source_ids,
                        denied_source_ids=args.denied_source_ids,
                        token_budget=args.token_budget)
    if args.brain_command == 'impact':
        from .impact import impact
        return impact(root, source_id=args.source_id, evidence_ref=args.evidence_ref,
                      receipt_id=args.receipt_id)
    from .portability import bootstrap, export_okf, private_handoff, release_kit
    if args.brain_command == 'export':
        return export_okf(root, args.output, public=args.public, write=not args.check)
    if args.brain_command == 'release-kit':
        return release_kit(root, args.output, write=not args.check)
    if args.brain_command == 'handoff':
        return private_handoff(root, args.output, write=not args.check)
    return bootstrap(root, args.source_root, apply=args.apply)


def run(args) -> int:
    try:
        result = dispatch(args)
        # Context is an intentional content result, never a journal or log.
        # Every other command emits metadata only.
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
        if getattr(args, 'check', False) and not result.get('current'):
            return 1
        if args.brain_command == 'evaluate':
            return 0 if result['accepted'] else 1
        return 0 if result.get('valid', True) else 1
    except Exception as exc:
        print(json.dumps({'valid': False, 'error': {'code': 'BRAIN_COMMAND_FAILED', 'type': type(exc).__name__}}))
        return 2
