# ACC 2027 final formatting note

The current local source uses IEEEtran only because ieeeconf.cls was not available in the execution environment used to build the verified draft.

Before PaperPlaza upload, use the official PaperPlaza class:

    \documentclass[letterpaper,10pt,conference]{ieeeconf}
    \IEEEoverridecommandlockouts
    \overrideIEEEmargins

Then compile, inspect every page again, and use PaperPlaza's full PDF test including page margins, searchability, image resolution, and font embedding.

Do not upload the current IEEEtran-compiled PDF as the final ACC submission without this template/compliance step.
