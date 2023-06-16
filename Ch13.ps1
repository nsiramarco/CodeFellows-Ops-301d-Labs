# Script Name:                  Powershell AD Automation
# Author:                       NATASHA SIRAMARCO
# Date of latest revision:      06/16/2023
# Purpose:                      In your Windows Server, access Powershell ISE.               
#                               Write a Powershell script that adds the below person to AD.
#                               Franz Ferdinand is the TPS Reporting Lead at GlobeX USA in Springfield, OR office. 
#                               Franz is part of the TPS Department. Franz’s email is ferdi@GlobeXpower.com.

# *****Key Note: this script is to be performed on the Powershell ISE*****

New-ADUser -Name "Franz Ferdinand" -City Springfield -Company "GlobeX USA" -Department TPS -DisplayName "Franz Ferdinand" - EmailAddress ferdi@GlobeXpower.com -Office Springfield -State OR -Title "TPS Reporting Lead"

