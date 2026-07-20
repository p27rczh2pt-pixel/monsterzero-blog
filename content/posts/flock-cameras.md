+++
date = '2026-07-20T09:00:00-05:00'
draft = false
title = 'Flock Cameras Are Everywhere Now, and Nobody Voted on It'
categories = ["surveillance"]
+++

Drive through most Texas towns now and you will pass at least one Flock Safety camera without knowing it. No blinking light, no sign, nothing that marks it as different from a traffic light or a road sign. It reads every license plate that passes, logs the time, the location, and details like bumper stickers or roof racks, and sends all of it to a searchable database. Cooke County has cameras like this too, installed without public notice, which is what got me looking into the company behind them.

## What Flock actually is

Flock Safety builds automated license plate reader cameras, known as ALPRs, and sells them to police departments, school districts, and homeowner associations. The company has more than 100,000 cameras running nationwide, scanning roughly 20 billion plates a month across 7,000 networks. Any single camera captures every car that passes, not just ones tied to a warrant or an active investigation.

The pitch to local governments centers on solving crimes and finding stolen cars. What gets left out of that pitch is the reach. Once a department joins Flock's network, more than 4,800 other law enforcement agencies nationwide can search that department's camera data too, unless someone actively opts out.

## What is actually inside one of these cameras

Independent teardowns have pulled a typical Flock camera apart piece by piece. Inside, you find a lithium-ion battery pack, a cellular modem for transmitting data without needing wired internet, a Wi-Fi and Bluetooth module, a GPS antenna, and a fixed 5-megapixel lens. Newer units run on an Android operating system with an unlocked bootloader, meaning the software protections a phone or tablet would normally have are simply not turned on.

That last detail matters more than it sounds. Researchers found a hidden diagnostic mode on some units, reachable by pressing a button on the camera in a specific sequence. That mode broadcasts its own Wi-Fi access point with an easily discoverable password and opens up web servers and video streams to anyone connected.

Sourcing is worth knowing too. Flock has promoted a domestic drone assembly facility in Georgia, but the camera hardware itself tells a different story. FCC filings tie the camera module used in Flock's network to a manufacturer based in the Futian District of Shenzhen, China, a manufacturing hub for electronics and camera components generally. The company acts as an original design manufacturer, meaning it builds the core hardware before Flock's branding goes on it. None of this makes the camera exceptional among consumer electronics, most of the industry sources parts from the same region, but it is worth knowing when the device is a government surveillance tool sitting on a pole in your neighborhood rather than a phone in your pocket.

## Cameras left wide open to the internet

In December 2025, technologist Benn Jordan and security researcher Jon "GainSec" Gaines found at least 60 of Flock's Condor pan-tilt-zoom cameras streaming live video to the open internet. No login, no password, no encryption. Anyone with the link could watch in real time, pull up a month of archived footage, and in some cases change camera settings. Jordan documented footage of unattended children on a playground, captured through one of the exposed feeds. He also showed how easily footage pulled from an exposed camera could be used to identify a specific person with basic open-source tools.

The exposure was not an isolated glitch. The same researchers had already published findings on how to gain full control of a Flock camera through physical access. Pressing a specific button sequence on the back of a unit opens a hidden wireless access point, and connecting to it lets someone enable Android Debug Bridge access and take over the device within minutes. On newer models, a small USB device plugged into an exposed port can do the same thing in about five seconds. The research also found that Flock does not require two-factor authentication for every police department using its system.

Flock's public response was that the company has never been hacked and that no data was leaked. Jordan told reporters the exposed cameras stayed reachable for days after Flock said the issue was fixed. Separately, credentials tied to Flock logins have reportedly turned up for sale on Russian cybercrime forums. In November 2025, Senators Ron Wyden and Raja Krishnamoorthi sent a formal letter asking the FTC to investigate.

What happened to the researchers afterward is its own warning sign. Gaines lost his job within 48 hours of publishing his findings. Jordan has said he was visited by police and photographed by people he believed to be private investigators outside his home. Publishing accurate, verifiable research about a company's public safety product led to consequences for the people doing the research, not fast fixes from the company being researched.

## Who is actually bankrolling Flock

Flock is privately held, not owned by any single company. Ownership sits with the three co-founders, Garrett Langley, Matt Feury, and Paige Todd, with Langley holding the largest individual stake as CEO, plus a long list of venture capital firms. The company has raised roughly $658 million to $1 billion depending on which funding tracker you check, across eight rounds, and was valued at $7.5 billion after its March 2025 raise, climbing to a reported $8.4 billion by April 2026.

Andreessen Horowitz has led the more recent rounds and anchored the $275 million raise in March 2025. Other backers include Greenoaks Capital, Bedrock Capital, Meritech Capital, Matrix Partners, Sands Capital, Kleiner Perkins, Tiger Global, Y Combinator, and Founders Fund, the venture firm Peter Thiel started in 2005. Thiel himself has no board seat at Flock and did not help start the company, so Founders Fund's stake makes him an indirect, minority financial backer at most, not someone steering the company.

What this means in practice: Flock answers to venture investors who backed the company at billion-dollar valuations expecting continued growth. That growth story depends on more cities signing contracts, more data flowing through the network, and more law enforcement agencies staying connected to it. Every dollar raised increases the pressure to keep expanding the footprint, which cuts directly against the local pushback happening in places like Norfolk, Dallas, and the string of cities canceling contracts.

## The pushback is real and it is growing

More than 80 cities and towns have deactivated cameras or canceled Flock contracts since the start of 2025. California is further along than most states here: a class action filed in San Francisco in February 2026 alleges out-of-state and federal agencies queried San Francisco's camera network more than 1.6 million times in seven months, a direct violation of the state's ALPR Privacy Act. The suit seeks $2,500 per violation.

Some residents have stopped waiting on city councils and courts entirely. Reporting from earlier this year documented Flock cameras getting physically dismantled in California, after a city council voted to keep them running despite a majority of residents at the meeting asking for a shutdown.

## The fight over whether any of this needs a warrant

None of this surveillance requires a warrant right now, and Flock is actively fighting in court to keep it that way. The core legal question traces back to Carpenter v. United States, a 2018 Supreme Court decision holding that police need a warrant to pull long-term cell phone location history, because that kind of data can reveal a person's whole pattern of life. Privacy advocates have been trying to extend that logic to networked license plate cameras ever since.

The clearest test case is Schmidt v. City of Norfolk. Two Norfolk, Virginia residents, backed by the Institute for Justice, sued the city in October 2024 over its roughly 175 to 200 Flock camera clusters, arguing that a city-wide camera dragnet tracking daily movement amounts to the same kind of warrantless search Carpenter was meant to prevent. A federal judge ruled against them in January 2026, reasoning that a rolling 21-day data retention window and limited camera coverage did not add up to the kind of exhaustive tracking the Supreme Court flagged in Carpenter. The judge explicitly rejected what's called the mosaic theory, the idea that many individually public observations can add up to an unconstitutional search when stitched together over time. The case is now on appeal to the Fourth Circuit, with the ACLU filing an amicus brief arguing the opposite: that ALPR networks like Flock's hand the government surveillance power the founders never anticipated and the Fourth Amendment was written to prevent.

Flock is not sitting on the sidelines of this fight. The company has published its own legal position paper arguing that fixed-location cameras with short retention windows fall outside Fourth Amendment protection entirely, and it promotes design choices like 30-day retention limits specifically because they help the company win these cases. That is a company actively shaping the legal argument that determines how much power its own product gets to wield without judicial oversight, and it has real money and legal staff behind that effort.

The ground under all of this may be shifting. The Supreme Court's 2026 ruling in Chatrie v. United States, involving a geofence warrant used to identify a bank robbery suspect through Google location data, found that police conducted a Fourth Amendment search when they pulled that data, and sent a related question back to the lower courts. Legal analysts are already watching for that ruling to ripple into the Norfolk appeal. Courts in other states have split on ALPR evidence too. New Hampshire has banned warrantless ALPR use outright, while federal courts in more than a dozen other states have upheld it. Nothing here is settled, which is exactly why Flock keeps fighting the legal argument as hard as it fights for new city contracts.

## Where Texas stands

Texas has no state law like California's ALPR Privacy Act restricting how this data moves between agencies. That gap is exactly why what happened in Kyle matters. The Kyle City Council voted 6 to 1 in April 2026 to apply for more state grant money to keep 38 existing Flock cameras running, even as neighboring communities were pulling back. Without a state privacy law, the decision to expand or restrict this technology sits entirely with local elected officials, which means it comes down to whoever shows up to the council meeting.

That is worth sitting with if you live somewhere with these cameras and never had a say in putting them up. Cooke County's cameras went in the same way most of these do nationwide, as a procurement decision, not a public vote. If you want to know whether your county's Flock network exists, how it is used, and who can search it, a Texas Public Information Act request to your county or local police department is the way to find out. I am filing one for Cooke County now.

## What to watch for, wherever you live

Check whether your city or county has a Flock contract, and whether it has a written policy limiting who can search the camera network and why. A policy on paper is not the same as enforcement, since audits in multiple cities have found searches that go beyond what the policy allowed. Ask which outside agencies have access to your local footage and how many searches they have run. Watch your city council agenda for Flock renewal or grant items, since these tend to move through with little public notice, the same way the original installations often did.