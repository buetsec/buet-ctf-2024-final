- Challenge Name: Admin Only
- Challenge Author: [marufmurtuza](https://marufmurtuza.github.io)
- Challenge Category: Android
- Challenge Difficulty: Easy
- Challenge Point: 100
- Challenge Flag: 
`BUETCTF{N3v3R_Ign0re_Th3_Manifest5_<GENERATED_HASH>}`

- Challenge Description:

```No Description```

[Admin_Only.apk](./Admin_Only.apk)


- Solution: 

```
Decompile the APK. Change the string value of 'isadmin' to 'yes' in AndroidManifest.xml. Recompile and Resign the APK. It will give the 'Get Real Flag' button to obtain the flag.
```