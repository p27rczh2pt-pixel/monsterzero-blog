+++
date = '2026-07-27T09:00:00-05:00'
draft = false
title = "Microsoft Wants to Sell You Data Integrity. It Might Be Part of the Problem."
categories = ["surveillance"]
+++
Microsoft has been on a real push lately to position itself as the company that will keep your data safe as AI takes over the workplace. It has a name for the pitch, the Secure Future Initiative, a growing suite of products to sell under it, Purview, Entra, Defender, and a fresh annual report, the Data Security Index, built to convince you the problem is real and Microsoft is the fix.

Worth looking a little closer at that pitch, because Microsoft's own recent history complicates it in three separate ways.

## The company selling the fix helped create the mess

Microsoft's 2026 Data Security Index surveyed more than 1,700 data security leaders across ten countries and landed on a central finding: AI adoption inside companies is outpacing the actual controls meant to secure it. Employees are feeding sensitive data into AI tools faster than anyone can govern where that data actually goes. Microsoft's answer is to sell more of its own stack on top of the problem: Purview for data governance, Entra for identity and access control, Defender for AI-specific threat detection.

Here's the awkward part. Microsoft's own AI products have been generating exactly this kind of incident. In late January 2026, Microsoft confirmed a bug in Microsoft 365 Copilot that let the AI assistant read and summarize emails marked "confidential," bypassing the data-loss-prevention safeguards specifically built to keep automated tools away from that content. The flaw lived in Copilot's "work tab" chat feature, the one that summarizes your sent and draft folders.

Recall is the more famous example. It's a Copilot+ PC feature that takes a screenshot of your screen every few seconds, encrypts it, and builds a searchable timeline of everything you've done on the computer, emails, private messages, financial documents, all of it. Microsoft calls it optional and says the data stays local. Privacy researchers weren't reassured. An AI and privacy advisor told the BBC the feature could be a "privacy nightmare," UK data regulators opened an inquiry, and even Elon Musk called it a "Black Mirror episode" and said he'd be turning it off. The design has a real gap too: if you turn Recall off but someone else using the same device has it enabled, your activity still gets captured through their session.

So the company telling enterprises they need better AI data governance is also the company whose flagship AI features keep needing to be walked back or patched for exactly the kind of exposure it's now selling protection against.

## Where "data integrity" runs into a harder question

Microsoft's AI security pitch gets tested by more than its own product bugs. It also gets tested by what the company actually does with its cloud infrastructure once a government customer starts using it at scale.

Leaked documents obtained by +972 Magazine, Local Call, and The Guardian showed that U.S. Immigration and Customs Enforcement's data storage on Microsoft Azure grew from around 400 terabytes in July 2025 to almost 1,400 terabytes by January 2026, a nearly fourfold increase in six months. The tools involved include Azure AI Video Indexer and Azure Vision, used for facial recognition, emotion detection, and object analysis of photo and video material.

None of that is unusual on its own. ICE is a federal law enforcement agency carrying out the enforcement responsibilities it's been assigned, and using modern cloud infrastructure to do that isn't inherently different from any other agency running its operations on Azure, AWS, or Google Cloud. The interesting part isn't that the growth happened, it's how Microsoft talks about it publicly.

Microsoft's official position is carefully worded: the company confirms it holds contracts with both ICE and DHS, but says it does not "presently maintain AI services contracts tied specifically to enforcement activities." That statement is narrower than it sounds, since it doesn't address whether the AI tools are available and in use within those agencies regardless of how the contract itself is labeled.

That phrasing matters more once you set it next to Microsoft's own stated principle elsewhere. In September 2025, Microsoft cut off Israel's Ministry of Defense from Azure access, citing documented mass surveillance concerns, with President Brad Smith stating plainly that Microsoft doesn't provide technology to facilitate mass surveillance of civilians. Whatever one thinks of ICE's mission, the question worth asking is a narrower one: does Microsoft apply that same standard evenly, or does the answer depend on which government is asking? A company that markets itself around "data integrity" and responsible AI governance should be able to answer that question the same way regardless of the customer.

## Own nothing, pay forever

There's a business model story underneath all of this too, and it's worth naming directly, since it shapes why Microsoft has so much leverage to push its AI governance stack onto customers in the first place.

Microsoft used to sell software the way most people still think software works: you bought a license, usually a boxed copy or a key, paid once, and owned that version indefinitely. Office 2010, Office 2013, Office 2019, these were capital purchases. You budgeted for them once, and Microsoft's revenue on that customer ended until the next upgrade cycle, whenever you chose to pay for one.

That model is functionally dead now. Starting with Office 365 in 2011 and accelerating hard through the 2010s, Microsoft moved its core productivity suite to a subscription structure, and it didn't stop there. Dynamics, its business applications suite, dropped perpetual licensing entirely, pushing customers toward Dynamics 365 in the cloud. By 2020, Microsoft had cut off older perpetually-licensed versions of Office from even connecting to Exchange Online, SharePoint, and other cloud services unless the software was on a current support lifecycle, a policy that wasn't marketed as forcing subscriptions, but had exactly that effect for organizations still running licenses they'd already paid for.

The mechanics of why this matters go beyond just "subscriptions cost more over time," though they often do. A subscription model converts a one-time capital expense into a recurring operating expense Microsoft controls the terms of indefinitely. Once your organization's email, documents, identity management, and collaboration tools all live inside a Microsoft subscription, walking away means rebuilding your entire technology stack, not just declining to buy the next version. That lock-in gets stronger every time Microsoft bundles another product into the same subscription tier, Teams, OneDrive, Entra identity management, Copilot itself. Microsoft's own licensing incentives push customers who commit heavily to Azure spend toward better bundled pricing elsewhere, which is a deliberate strategy to make the whole stack, productivity, identity, cloud infrastructure, AI, mutually reinforcing and hard to unwind from.

And because it's a subscription, you're permanently exposed to price changes in a way perpetual licensing never allowed. A perpetual license, once bought, was a done deal. In a subscription model, when Microsoft raises the per-user monthly price, and it has, that cost lands on your budget at the next renewal whether you planned for it or not. There's no "keep using the old version at the old price" option anymore, because there is no version you own, only ongoing access you're renting.

This is the same underlying pattern the rest of this post is about, just applied to money instead of data. Microsoft's pitch is always continuity, security, and staying current. What that pitch obscures is that the company has restructured its entire business around making sure customers never actually own anything, and never fully leave, which is exactly the kind of leverage that makes it easier to sell an entire enterprise on Purview, Entra, and Defender as the "complete" solution, not because it's necessarily the best one, but because switching away from any piece of an all-in Microsoft subscription is now a much bigger decision than it used to be.

## The credibility problem underneath all of it

If you're wondering why Microsoft suddenly cares so much about being seen as the security-first AI company, a lot of it traces back to a genuinely bad 2023 breach that's still shaping the company's messaging today.

A Chinese state-linked group tracked as Storm-0558 stole a Microsoft cryptographic signing key and used it to forge authentication tokens, gaining access to Exchange Online email accounts at roughly 25 organizations. The victims weren't random: Commerce Secretary Gina Raimondo, the U.S. Ambassador to China, and a member of Congress were among those whose email got read. The federal Cyber Safety Review Board's independent investigation didn't hold back. It found the breach was entirely preventable, that Microsoft's security culture was "inadequate and requires an overhaul," and, months into the investigation, that Microsoft still didn't actually know how the signing key had been stolen in the first place, despite earlier public statements suggesting otherwise. The board also found Microsoft had made inaccurate public statements during the incident that later needed correcting.

One more detail worth sitting with: the breach was only caught because the State Department happened to have a premium logging tier enabled, letting its own security team spot the anomalous access. Lower-tier Microsoft 365 customers didn't have that visibility at all. Only after the incident, and after pressure that reportedly included the federal government itself, did Microsoft make that audit logging free to all customers rather than something you had to pay extra for.

Microsoft's Secure Future Initiative, the same program now underpinning its AI security marketing, was created directly in response to this failure. That's not necessarily a knock against the initiative itself, real reforms can come out of real failures. But it's useful context for understanding why Microsoft is spending 2026 so aggressively positioning itself as the trustworthy steward of enterprise AI data. It's rebuilding credibility it lost in a very concrete, well-documented way, at the same time its current AI products keep generating smaller versions of the same basic problem: data ending up somewhere it wasn't supposed to be, discovered by the customer rather than the company.

## Where that leaves things

None of this means Purview or Entra or Defender are bad products, or that every company using them is making a mistake. Plenty of the underlying data governance problems these tools address are real, and Microsoft isn't wrong that AI adoption is outpacing security controls industry-wide.

But it's worth separating the marketing from the track record before buying into either. The company pitching itself as the fix for AI-era data sprawl is also the company whose own Copilot and Recall features have needed public walk-backs for the same category of exposure, whose public statements about government cloud contracts are narrower than they first appear, whose business model has quietly shifted toward permanent recurring access rather than ownership, and whose current security push exists largely because of a previous, well-documented failure that let a foreign intelligence service read the U.S. State Department's email for weeks before anyone at Microsoft noticed.

Data integrity is a real problem. Whether the company most loudly selling the solution has actually earned that role yet is a fair question to keep asking.