# !!!Warning - This Project is no longer maintained!!!

This project has been superceded by functionality now in [OPAL](https://github.com/openhealthcare/opal) core, and is no longer being actively maintained.

Users are advised not to use this code in their projects.

### Begin Original README

This is analytics - an [OPAL](https://github.com/openhealthcare/opal) plugin.

## Installation

1. Add to your application's INSTALLED_APPLICATIONS.

2. Create the settings (for your tracking ID/backend)

3. Spend an hour watching yourself click things on a realtime analytics dashboard 
thanks to the magic of the internet.

## Settings

### OPAL_ANALYTICS_ID 

This is the Tracking ID for your application - e.g. for Google Analytics it's a
string like 'UA-XXXXX-X'

### OPAL_ANALYTICS_BACKEND

(default == Google Analytics)

If set, the OPAL_ANALYTICS_BACKEND will update your backend to work with 
any of the following:

* google.analytics
* piwik

### OPAL_ANALYTICS_NODOMAIN 

(default = False)

If set to True, this will enable analytics on e.g. localhost servers
for testing purposes.

