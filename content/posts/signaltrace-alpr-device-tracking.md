---
title: "Your License Plate Camera Is About to Start Tracking Your Phone Too"
date: 2026-08-21T14:00:00-05:00
draft: false
tags: ["surveillance", "Leonardo", "SignalTrace", "ALPR", "privacy"]
categories: ["surveillance"]
description: "A defense contractor is bolting Bluetooth, WiFi, and RFID tracking onto license plate cameras already installed across the country. Here's what SignalTrace actually does."
---

Every conversation I've had this week about license plate cameras eventually landed on the same question from someone in the comments: does this stuff monitor phones too? Up until a few weeks ago, my honest answer was no. That answer is now out of date.

## What SignalTrace actually is

In June 2026, 404 Media broke the story on a product called SignalTrace, built by Leonardo, an Italian aerospace and defense conglomerate that already owns ELSAG, one of the established license plate reader brands competing directly with Flock and Axon in the American market. Leonardo isn't a scrappy startup chasing a government contract. It's a €17.8 billion company, roughly 30 percent owned by the Italian government itself, with 60,500 employees and subsidiaries spanning fighter jets, satellites, and missile systems. This is a serious, well-funded player, not a fringe vendor.

SignalTrace is an add-on layer for existing ALPR cameras. Instead of just photographing your license plate, it also captures the wireless signals broadcasting from every device near your car as you drive past: your phone, your Bluetooth earbuds, your smartwatch, your car's own infotainment system, tire pressure sensors, employee badges, and, according to Leonardo's own marketing material, pet microchips. Every one of those devices constantly broadcasts a low-level identifying signal just by existing in your pocket or your car. SignalTrace turns that broadcast into what the company calls an "electronic fingerprint" and ties it to your license plate and the time and place you were photographed.

## The evolution nobody voted on

License plate readers didn't start out as anything close to this. The first generation of these cameras did exactly one thing: photograph a plate, check it against a hotlist, alert an officer to a stolen vehicle or an outstanding warrant. That was the entire pitch, and it's the version most city councils actually approved when they first signed a contract.

That's not where the technology stayed. Flock added gunshot-detection microphones to its pole network, then tried expanding those microphones to detect screaming and other "human distress" sounds before public pressure forced a partial retreat. Axon built its own competing plate reader line and layered in AI-written police reports, real-time video analysis, and a fleet of drones dispatched automatically to 911 calls. Each of those additions arrived the same way: bolted onto infrastructure that was already approved, sold to a customer base that already existed, without a new public vote on whether the expanded capability was something residents actually wanted.

SignalTrace is the next rung on that same ladder, and arguably the most consequential one yet, because it changes what the network is fundamentally capable of identifying. A camera that reads plates is limited to vehicles. A camera that fingerprints Bluetooth and WiFi signals identifies people directly, whether they're driving, riding along, or just walking past a sensor with a phone in their pocket. That's not a modest feature update. It's the difference between a system that tracks cars and a system that tracks you.

## Why this is a real escalation, not just more of the same

License plate readers already raised real concerns on their own: permanent records of where your car has been, retained for weeks, searchable without a warrant in most states. SignalTrace changes what the system is actually trying to identify. Leonardo's own language describes the goal as identifying "groups of consumer electronic devices that routinely travel together." The company isn't hiding the intent here. One of their own product materials uses the example of a hundred cars passing a sensor, with the system flagging the one device that consistently shows up across multiple different vehicles, a person, not a car, being tracked regardless of what they're driving or who they're riding with.

That's the actual shift. A license plate belongs to a vehicle. A phone belongs to a person. Once a network can reliably tie a specific person's device signature to a vehicle, and then follow that signature across different vehicles over time, the system has stopped tracking cars and started tracking individuals directly, including passengers who were never driving at all and never gave anyone their information.

## What Leonardo says, and why it doesn't settle much

Leonardo's own materials make a specific defense: the system doesn't decrypt device content or read the substance of anyone's communications, it only captures broadcast identifiers. That's true as far as it goes, and worth taking at face value rather than exaggerating. Nobody's phone calls or text messages are being read by a sensor on a highway pole.

But that defense answers a question nobody was really asking. The privacy concern with a tool like this was never primarily about reading message content. It's about whether a government contractor or a police database can connect a person, a device, a vehicle, a location, a time, and a group of people moving together, and hold that connection indefinitely, searchable, without anyone in that chain ever having done anything wrong. SignalTrace's own marketing confirms that's exactly the point: bridging the gap between a vehicle and the people inside it.

Leonardo also points to audit logging and access controls as safeguards, the system stores data until a specific investigator makes a request, and all user activity is supposedly logged and auditable. If that sounds familiar, it should. It's the identical framing Flock uses to defend its own plate reader network, and it has the identical weakness. Audit logs tell you who misused a system after the harm already happened. They don't stop the misuse from occurring in the first place, and they say nothing at all about whether the underlying collection should have happened without a warrant to begin with.

## The legal ground here is genuinely unsettled

There's no federal law that explicitly prohibits this kind of device fingerprinting. The strongest legal analogy available right now is Carpenter v. United States, the 2018 Supreme Court decision requiring a warrant before police can access someone's historical cell-site location data. The Court's reasoning wasn't about whether any single data point was private, it was that aggregating someone's movements over time reveals a detailed picture of their life that no single observation ever could, and that aggregation itself creates a privacy interest the Fourth Amendment protects.

SignalTrace is Carpenter's underlying concern turned into a commercial product and sold directly to local police departments and retail loss-prevention teams, with no court ruling yet on whether this specific application requires a warrant at all.

## It's already being sold, right now

This isn't a prototype or a concept pitch. Leonardo is actively marketing SignalTrace to law enforcement agencies and, separately, to retail security clients for tracking "suspects'" devices in store parking lots, entirely outside any government or law enforcement context whatsoever. It plugs directly into Leonardo's existing Enterprise Operations Center software, the same platform many agencies already use to manage their current ALPR data, meaning any department that already has Leonardo's camera infrastructure installed can potentially add this capability without a separate, publicly debated purchase decision. The infrastructure is already standing. This is a software layer being added on top of it.

## Where this leaves the broader conversation

I've spent a lot of time on this blog walking through Flock, Axon, and the Texas cell-site simulator program the state just bought, each one a different vendor, a different contract, a different city council meeting nobody attended. SignalTrace is the clearest example yet of the actual mechanism behind all of it: infrastructure gets approved once, under one stated purpose, and years later a new capability gets bolted onto the same hardware, sold to the same customers, without any new public vote or debate about whether that expanded capability is something the community actually wants.

Nobody voted on whether their license plate camera should also fingerprint their phone. Most people don't know it's happening yet. By the time it's common knowledge, in most places it'll already be running.
