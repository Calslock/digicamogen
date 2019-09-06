# digicamogen
My first simple project using Python. Script generates .png file with digital camouflage-like pattern in same folder it was run. 

## example usage
```
$ python3 digicamogen.py --width 512 --height 512 --prob 20
```

## arguments
`-W [number], --width [number]` - width of generated image in pixels (default: 256px)  
`-H [number], --height [number]` - height of generated image in pixels (default: 256px)  
`-C [hex], --color [hex]` - color of strokes in image in hex (default: b877b4)  
`-F [name], --filename [hex]` - name of generated file (default: camo)  
`-P [number], --prob [number]` - variance in colors - the greater this value, the pattern will look more stripe-like, and less noise-like. (default: 10)  
