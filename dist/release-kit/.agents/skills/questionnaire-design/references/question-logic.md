# Question logic

The active contract uses `depends_on: null` or an object with exactly
`question_id` and `equals`. The dependency references a stable question ID and
the graph must remain acyclic. Explain relationships that need richer logic in
the proposal review instead of embedding a rules engine in the note.

Selection questions require at least two options with stable values and equivalent English/French labels. Avoid an option whose meaning overlaps another option.

An update preserves its question ID only when decision intent, evidence scope,
and answer semantics remain compatible. Otherwise propose a new ID, deprecate
the old note only after approval, and preserve its history.
