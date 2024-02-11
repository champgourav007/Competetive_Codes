# Need for configure App with Access Policy
  * For some Microsoft Restful API's only the delegated Access Token are required for calling, but to bypass this delegated flow by ```client_credentials```, we need to ad the policy for the App to take the access token on behalf of the user.
  
  * You can use the cloud communications API in Microsoft Graph to configure an application access policy that allows applications to access online meetings on behalf of a user.

  * In some cases, such as for background services or daemon apps that run on a server without the presence of a signed-in user, it is appropriate for an app to call Microsoft Graph to take actions on behalf of a user. For example, an app might need to call ```Microsoft Graph``` to schedule multiple meetings based on published schedules (such as courses) or external scheduling tools. In these cases, the user that the application acts on behalf of is identified as the meeting organizer.

  * Administrators who want to allow an application to access online meeting resources on behalf of a user can use the ```New-CsApplicationAccessPolicy``` and ```Grant-CsApplicationAccessPolicy``` PowerShell cmdlets to configure access control.

  * This article covers the basic steps to configure an application access policy. These steps are specific to online meetings and do not apply to other Microsoft Graph resources.

# Steps to Add the Policy
```Note: You need to be Admin to do this```

  1. Make sure you have  ```PowerShell version 5.1 and more``` to check type ```$PSVersionTable.PSVersion``` cmd to powershell. To install latest version please refer Microsoft Docs.
  2. ```Install-Module -Name MicrosoftTeams -Force -AllowClobber``` to install microsoft teams.
  3. ```Import-Module MicrosoftTeams``` to import the module.
  4. ```Connect-MicrosoftTeams``` connect to the admin account.
  5. ```New-CsApplicationAccessPolicy -Identity Test-policy -AppIds "client_id/add_id" -Description "description here"```  to add new ploicy for the App Service.
  6. ```Grant-CsApplicationAccessPolicy -PolicyName Test-policy -Identity "user_id"``` to grant the policy to the user.
  OR
  ```Grant-CsApplicationAccessPolicy -PolicyName Test-policy -Global``` to grant the policy to all the users.
   