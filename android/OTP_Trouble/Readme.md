- Challenge Name: OTP Trouble
- Challenge Author: [marufmurtuza](https://marufmurtuza.github.io)
- Challenge Category: Android
- Challenge Difficulty: Medium
- Challenge Point: 200
- Challenge Flag: 
`BUETCTF{0Tp_5h0uld_Always_be_Generat3d_In_Server_Side_<GENERATED_HASH>}`

- Challenge Description:

```This app is for only admins. Are you an admin?```

[OTP_Trouble.apk](./OTP_Trouble.apk)


- Solution: 

```
Open the app and filter the logs of the device.
Using two filter is recommended.
(To get the OTP easily)    Filter-1: logcat | grep flutter          
(To get the app signature) Filter-2: logcat | grep 'com.bcf.otp_trouble'

Collect the OTP and the app signature.

Send an sms in the following format to the device:
<#> Your OTP for BCF24 is <OTP_Here> <App_Signature_Here>

This will autofill the OTP Field in the application.
```
