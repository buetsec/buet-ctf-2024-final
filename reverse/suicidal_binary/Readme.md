- Challenge Name: Suicidal Binary
- Challenge Author: [marufmurtuza](https://marufmurtuza.github.io)
- Challenge Category: Reverse
- Challenge Difficulty: Easy
- Challenge Point: 100 (Dynamic)
- Challenge Flag:
  `BUETCTF{Y0u_5av3d_th3_5uicida1_biNary_bUt_At_wh4t_c05t?_<GENERATED_HASH>}`

- Challenge Description:

`Can you save the binary from suiciding?`

[Suicidal_Binary.exe](./Suicidal_Binary.exe)

- Solution:

```
Analyze the binary without executing. (Otherwise it will delete itself if it finds it is being debugged)
Find the flag function.
Patch the binary by creating a jump to the flag function from the main function.
```
