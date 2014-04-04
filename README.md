Abstraction is considered a fundamental tenet of scalable engineering,
and we often enforce abstraction through mechanisms like information
hiding.  The ability to enforce abstraction in this way is often
considered an important language feature for large software projects,
and when abstractions are security critical, this enforcement is
mandatory.

However, real software engineers regularly, repeatedly and profitably
violate abstraction (and information hiding).  Mainstream program
languages provide a variety of mechanisms for violating information
hiding mechanisms, and languages that are too inflexible to allow
such violations often force programmers to resort to techniques that
are even worse than the disease.

We are investigating programming languages which allow abstraction to be
violated in a principled way.  Our approach is twofold: first, we want
to describe large, existing software ecosystems (web browsers and
extensions, operating systems, Emacs, etc) which exemplify an "open"
universe of code, and understand why these systems have been as
extensible as they have been.  Second, we want to argue that existing,
well-understood programming languages theory (compiler correctness,
monads, continuations, dynamic scoping, etc) can serve as the foundation
for programming languages which let you reach inside the black box, when
you need to.
