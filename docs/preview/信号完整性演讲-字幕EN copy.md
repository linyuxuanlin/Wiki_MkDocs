in a

real channel

frequency dependent changes in the

components of a signal

can lead to changes in the received

signal shape and this can make it harder

for the receiver

to correctly detect the transmitted

signal level or to determine its state

and as we'll see later in this

presentation it's usually the higher

frequency components that are attenuated

more than the lower frequency components

channels can have different physical

formats one of the most common types of

channels is a trace on a printed circuit

board

or pcb the channel can also be in the

form of connectors

between different boards or even cables

between different components or systems

the principles of signal integrity and

the way that degradations are measured

or quantified

apply to all of these different channel

formats but in this presentation

we'll be using pcb traces for most of

our examples

in order to better understand signal

integrity we're going to take a look at

four of the most common forms of channel

degradation

impedance mismatches frequency response

crosstalk and noise there are many other

factors involved in signal integrity

but these are among most important for

high-speed digital design

to minimize degradations a signal should

see a constant impedance along the path

or trace

remember that impedance is a point

concept so there's no guarantee that the

impedance in the middle of a trace

will be the same as the impedance at the

beginning or the end of a trace

if there is an impedance mismatch or

change at any point

this can cause reflections which in turn

lead to signal distortion

there are many different sources of

mismatch on a printed circuit board

changing the dimensions geometry or

direction of pcb traces

is a common cause this includes things

such as the presence of branches or

t's improper terminations or

unterminated stubs can also cause

reflections

the characteristics of a via such as

hole size pad size etc

will also affect its characteristic

impedance discontinuities

such as those caused by device pins

variation in the pcb board materials

and the return path taken by the current

are other common causes of impedance

mismatches on printed circuit boards

signals may also be distorted due to

frequency specific attenuation

remember that attenuation or loss

usually increases as frequency increases

if the loss were uniform for all

frequency components the received signal

shape would remain the same

but when only the higher frequency

components are attenuated this can cause

distortion of the transmitted waveform

as it moves through the channel

one of the more common sources of

frequency dependent loss

is the resistance of the conductors

themselves in addition

the characteristics of pcb materials

will also create different dielectric

losses

at different frequencies an additional

source of frequency dependent

attenuation

is a so-called skin effect this refers

to the phenomenon whereby higher

frequency signals

travel closer to the outside of a

conductor rather than within it

this in turn creates self-inductance

which increases with frequency

and leads to additional attenuation

increasing the width of a trace to

increase its overall surface area

can reduce loss caused by the skin

effect but as we've just seen

changing trace geometry also creates

impedance issues

and this is an excellent example of the

kinds of compromises that are often

encountered

when designing for signal integrity

crosstalk refers to the coupling of

energy between adjacent conductors or

traces

it's largely a function of geometric

dimensions and positioning

crosstalk can be created either by

mutual inductance and or

mutual capacitance often the terms

aggressor and

victim are used when describing this

coupling of energy

in near-end crosstalk the signal

coupling occurs close to the aggressor's

transmitter

in far end crosstalk this coupling

occurs at the

far end of the aggressor's trace and

just as with other aspects of signal

integrity

crosstalk becomes a greater problem as

signal rise time decreases

there are a number of different ways of

minimizing crosstalk

increasing the separation or distance

between the traces

minimizing the length of parallel trace

runs and

placing conductors close to the ground

plane are some of the more common

ways of minimizing crosstalk in pcb

designs

crosstalk could be considered an example

of noise since

crosstalk is an undesired external

voltage that is coupled onto our

transmitted signal as you might imagine

external noise that couples onto our

signal can cause a number of problems

the most important one being that it

lowers the signal-to-noise ratio at the

receiver

another common source of noise that

contributes to signal integrity issues

is noise introduced by the power supply

and therefore

power integrity can be an important

factor in overall signal integrity

noise can also occur in the form of

electromagnetic interference or

emi that's coupled in either from

external

or internal sources of noise you may

also hear this referred to as emc

or electromagnetic compatibility which

also influences overall

signal integrity

another very important topic in signal

integrity is something called

jitter jitter can be defined as

variations in the timing of the signal

digital data signals are sampled at

defined intervals or bit times

where we use voltage levels at those

times to decide if we received

a 1 or a0 if the signal needs to

transition between states

this transition must occur between the

sample times

variations in timing can lead to

undefined or incorrect values of the

sample times

and this in turn can create bit errors

there are many different types of jitter

such as data dependent jitter periodic

jitter

random jitter etc as mentioned a moment

ago

jitter is a very large but very

important topic

so please see our separate presentations

on jitter if you'd like to learn more

when it comes to testing for signal

integrity there are two complementary

aspects

simulation and test and measurement

let's look at each of these topics in a

bit more detail

simulation is important because it would

be very expensive and time consuming

if you made an actual physical board

tested it for any possible signal

integrity issues

and then repeated the process for each

redesigned board

simulation is used to produce output

waveforms based on models of a system

or system components it's performed

using special software tools

in part because the calculations would

be much too complex to do by hand

the output waveforms are calculated

using models of frequency dependent

behavior

simulation therefore helps us to make

good design decisions

and reduces the probability of signal

integrity issues

the two primary tests and measurement

instruments used in signal integrity

are oscilloscopes and vector network

analyzers or vnas

oscilloscopes are primarily used for

time domain analysis of waveforms

scopes usually have a relatively high

input voltage range

and are used to measure jitter and

so-called eye diagrams

which we'll look at on the next slide a

vna

on the other hand is primarily a

frequency domain instrument

vnas have a high dynamic range which is

useful for measuring things like far end

crosstalk

vnas can make s-parameter and tdr

measurements as well

when it comes to signal integrity

testing one could say that oscilloscopes

are used to measure the waveform

and vnas are used to measure the channel

but in recent years

this distinction has become somewhat

blurred for example

some vnas can use frequency domain

information to generate eye diagrams

and eye diagrams are an important

quality measurement in signal integrity

testing

eye diagrams are used to assess the

quality of transitions between different

voltage states

in other words how cleanly does a signal

transition from a

0 to a 1 or vice versa they can also

provide numeric information on

parameters such as

rise time signal amplitudes noise levels

etc

eye diagrams are created by enabling

persistence and overlaying multiple

periods of a signal

degradations will close or narrow the

eye

and often the nature or cause of this

closing or narrowing

can be determined by visual inspection

of the eye

in addition masks can be used to

quantify this level of closure

a mask is defined as a region or regions

where the signal should not enter

and a failure can be defined as any time

the mask is violated

eye diagrams and masks are fundamental

tools in signal integrity testing

and therefore standards will often

specify the characteristics

of the mask to be used during testing

let's look at eye diagrams made at

various points along a printed circuit

board between the transmitter

and the receiver at the transmitter we

see a wide

relatively open eye diagram as a signal

moves through the channel

the eye will often narrow vertically and

or horizontally

if the necessary steps are not taken to

ensure adequate signal integrity

eye closure may prevent the receiver

from being able to correctly recover the

transmitted signal

let's end with a brief summary single

integrity is an important consideration

especially in high-speed digital design

and this is primarily due to the shorter

signal rise times found in most

high-speed systems

degradation of the signal can occur at

any point along the signal chain

that is in the transmitter the channel

and or the receiver

examples of common channel degradations

discussed in this presentation

included impedance mismatches frequency

response

crosstalk and noise and although we only

briefly touched on it in this

presentation

jitter is another important topic in

signal integrity

there are several ways to test and

troubleshoot signal integrity issues

simulation is often used to model or to

predict problems in the early design

phases

whereas both oscilloscopes and vector

network analyzers

can be used to quantify signal integrity

in actual physical systems

in particular eye diagrams and masks are

very often used

in identifying and measuring the types

and levels of signal degradations

this concludes our presentation

understanding single integrity

if you'd like to learn more about signal

integrity or how signal integrity is

tested

please see the links in the video

description thanks for watching
