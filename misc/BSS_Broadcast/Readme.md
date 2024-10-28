- Challenge Name: BSS Broadcast
- Challenge Author: [marufmurtuza](https://marufmurtuza.github.io)
- Challenge Category: Misc
- Challenge Difficulty: Easy
- Challenge Flag: 
`BUETCTF{SSTV_broadcast_from_bcf_imaginary_space_station}`

- Challenge Description:

```Lily was working on the ground station of BCF Astronomical Research Facility. One day she recieved a strange signal. She thought it was a signal from the aliens? But is that so?```

[Signal.wav](./signal.wav)


- Solution: 

```
Tool: https://github.com/colaclanth/sstv

sstv -d signal.wav -o output.png
```