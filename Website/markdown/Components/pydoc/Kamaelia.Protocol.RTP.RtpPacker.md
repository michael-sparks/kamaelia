---
pagename: Components/pydoc/Kamaelia.Protocol.RTP.RtpPacker
last-modified-date: 2009-06-05
page-template: default
page-type: text/markdown
page-status: current|legacy|needsupdate|deprecated|recommended
---
::: {.container}
::: {.section}
[Kamaelia](/Components/pydoc/Kamaelia.html){.reference}.[Protocol](/Components/pydoc/Kamaelia.Protocol.html){.reference}.[RTP](/Components/pydoc/Kamaelia.Protocol.RTP.html){.reference}.[RtpPacker](/Components/pydoc/Kamaelia.Protocol.RTP.RtpPacker.html){.reference}
========================================================================================================================================================================================================================================================================
:::

::: {.section}
::: {.container}
-   **component
    [RtpPacker](/Components/pydoc/Kamaelia.Protocol.RTP.RtpPacker.RtpPacker.html){.reference}**
:::

-   [RtpPacker Component](#635){.reference}
:::

::: {.section}
RtpPacker Component {#635}
===================

Takes data from a preframer:

> -   Creates an RTP Header Object
> -   Uses the timestamp & sample count to generate an RTP timestamp
:::

------------------------------------------------------------------------

::: {.section}
[Kamaelia](/Components/pydoc/Kamaelia.html){.reference}.[Protocol](/Components/pydoc/Kamaelia.Protocol.html){.reference}.[RTP](/Components/pydoc/Kamaelia.Protocol.RTP.html){.reference}.[RtpPacker](/Components/pydoc/Kamaelia.Protocol.RTP.RtpPacker.html){.reference}.[RtpPacker](/Components/pydoc/Kamaelia.Protocol.RTP.RtpPacker.RtpPacker.html){.reference}
==================================================================================================================================================================================================================================================================================================================================================================

::: {.section}
class RtpPacker([Axon.Component.component](/Docs/Axon/Axon.Component.component.html){.reference}) {#symbol-RtpPacker}
-------------------------------------------------------------------------------------------------

::: {.section}
### [Inboxes]{#symbol-RtpPacker.Inboxes}

-   **(\'inbox\', \'\')** : Code uses old style inbox/outbox
    description - no metadata available
:::

::: {.section}
### [Outboxes]{#symbol-RtpPacker.Outboxes}

-   **(\'outbox\', \'\')** : Code uses old style inbox/outbox
    description - no metadata available
:::

::: {.section}
### Methods defined here

::: {.container}
::: {.boxright}
**Warning!**

You should be using the inbox/outbox interface, not these methods
(except construction). This documentation is designed as a roadmap as to
their functionalilty for maintainers and new component developers.
:::
:::

::: {.section}
#### [\_\_init\_\_(self, label, looptimes\[, selfstart\])]{#symbol-RtpPacker.__init__}
:::

::: {.section}
#### [closeDownComponent(self)]{#symbol-RtpPacker.closeDownComponent}

closeDownComponent
:::

::: {.section}
#### [initialiseComponent(self)]{#symbol-RtpPacker.initialiseComponent}
:::

::: {.section}
#### [mainBody(self)]{#symbol-RtpPacker.mainBody}
:::
:::

::: {.section}
:::
:::
:::
:::

::: {.section}
Feedback
========

Got a problem with the documentation? Something unclear that could be
clearer? Want to help improve it? Constructive criticism is very welcome
- especially if you can suggest a better rewording!

Please leave you feedback
[here](../../../cgi-bin/blog/blog.cgi?rm=viewpost&nodeid=1142023701){.reference}
in reply to the documentation thread in the Kamaelia blog.
:::

*\-- Automatic documentation generator, 05 Jun 2009 at 03:01:38 UTC/GMT*