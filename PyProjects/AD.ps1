# This is a test powershell script to access and do cool stuff with AD
<#
TO DO
- Search for user
- Find status of user (which status is most used?)
    - Account un/locked
    - Password Reset
    - Change Address
    - Change Phone
- Add user
- Delete user...?
- Reset Password
- Change number
- Add to group...?
#>
Import-Module ActiveDirectory
<#function Change-Phone($User, $Domain, $AdminCred) #DON'T USE. Changing AD may cause weird things to happen. Everything is part of a ecosystem
{
    #Gets, confirms and changes mobile number!
    $Mobile = Get-ADUser -Identity "$User" -Server "$Domain" -Properties mobile | Select -Expand mobile
    Write-Host "Current mobile number is: $Mobile"
    
    $ReallyChange = Read-Host -Prompt "You sure you want to change ${Mobile}? Y/N"
    If($ReallyChange -eq "Y" -or $ReallyChange -eq "y")
    {
        $NewMobile = Read-Host -Prompt "Please enter new number (Format: 123-456-7891)"
        Set-ADUser -Identity $User -Server $Domain -Credential ($DomainName + $AdminUser) -mobile $NewMobile
    }
    Else{
        Write "Mobile number not changed"
    }
}

function Change-Address($User, $Domain, $AdminUser) #DON'T USE. Changing AD may cause weird things to happen. Everything is part of a ecosystem
{
    #This gets user address!
    $Street = Get-ADUser -Identity "$User" -Server "$Domain" -Properties StreetAddress | Select -Expand StreetAddress
    $City = Get-ADUser -Identity "$User" -Server "$Domain" -Properties City | Select -Expand City
    $Postal = Get-ADUser -Identity "$User" -Server "$Domain" -Properties PostalCode | Select -Expand PostalCode
    $ConfirmChange = Read-Host -Prompt "You sure you want to change ${Street}, ${City}, ${Postal}? Y/N"
    
    #This changes address, after confirmation!
    If($ConfirmChange -eq "Y" -or $ConfirmChange -eq "y")
    {
        $NewAddress = Read-Host -Prompt "Please enter new address (Format: Street, City, PostalCode)"
        $Street, $City, $Postal = $NewAddress.split(',', 3)
        Set-ADUser -Identity $User -Server $Domain -Credential ($DomainName + $AdminUser) -StreetAddress $Street -City $City -PostalCode $Postal
    }
    Else{
        Write "Address not changed"
    }
}
#>
function Reset-Pass($User, $Domain, $AdminUser) #DON'T USE. Changing AD may cause weird things to happen. Everything is part of a ecosystem. Use go/sspm
{
    $ReallyChange = Read-Host -Prompt "Are you sure you want to change the password? Y/N"
    $Affirm = @("y", "Y", "Yes", "yes")
    $Finished = $False
    If ($Affirm -contains $ReallyChange){
        While ($Finished -ne $True) {
            $NewPass = Read-Host "Please enter new password" -AsSecureString
            $Confirmation = Read-Host "Please re-enter new password" -AsSecureString
            $Ptr = [System.Runtime.InteropServices.Marshal]::SecureStringToCoTaskMemUnicode($NewPass)
            $result = [System.Runtime.InteropServices.Marshal]::PtrToStringUni($Ptr)
            [System.Runtime.InteropServices.Marshal]::ZeroFreeCoTaskMemUnicode($Ptr)
            
            $Ptr1 = [System.Runtime.InteropServices.Marshal]::SecureStringToCoTaskMemUnicode($Confirmation)
            $result1 = [System.Runtime.InteropServices.Marshal]::PtrToStringUni($Ptr1)
            [System.Runtime.InteropServices.Marshal]::ZeroFreeCoTaskMemUnicode($Ptr1)
            $ReallySame = $result.CompareTo($result1)
            
            If ($ReallySame -eq 0) {
                Set-ADAccountPassword -Reset -Identity $User -Server $Domain -Credential ($DomainName + $AdminUser) -NewPassword $NewPass
                $Finished = $True
            }
            Else{
                Write "Error. Mistyped new password."
                $Again = Read-Host -Prompt "Try again? Y/N"
                If ($Affirm -NotContains $Again) {
                    $Finished = $True
                }
            }
        }
    }
    Else {
        Write "Going back to main menu"
    }
    
}

function Check-Locked-Status($User, $Domain, $AdminUser) #works. NEED ADMIN
{
    #Checks if locked out or not
    $IsLockedOut = Get-ADUser -Identity $User -Server $Domain -Properties LockedOut | Select -Expand LockedOut
    If ($IsLockedOut) {
        Write "$User is locked out!"
        Write "Unlocking account..."
        Unlock-ADAccount -Identity $User -Server $Domain -Credential ($DomainName + $AdminUser)
        Write "$User unlocked."
    }
    Else{
        Write "$User is NOT locked out."
    } 
}

function Choose-Domain(){
    $Domain = Read-Host -Prompt "
------------------------------------------------------------------------------  
Defaults to BlackBerry RIMNET
    [1] BlackBerry RIMNET (rim.net)
    [2] Good Tech SPRINGTHINGS (corp.good.com)
Please choose domain number"

    If($Domain -eq "2") {
        $Domain = "corp.good.com"
        $DomainName = "SPRINGTHINGS\"
        }
    Else {
        $Domain = "rim.net" 
        $DomainName = "RIMNET\"
        }
    $AdminUser = Read-Host -Prompt "Please enter your [$Domain] admin username"
    
    $AdminUser 
    $Domain
    $DomainName
    return #Returns the above three. Gotta separate them out when you call the function!
}

$DomainDetails = Choose-Domain

$AdminUser  = $DomainDetails[0]
$Domain     = $DomainDetails[1]
$DomainName = $DomainDetails[2]
    
function Main-Menu(){
    $Done = $false
    While($Done -ne $True) {
        $User = Read-Host "Please enter the [$Domain] username you wish to access or [c] to change domain or [q] to quit
"

        If ($User -eq "q" -or $User -eq "Q") {
            Write "Goodbye"
            $Done = $True
        }
        Elseif ($User -eq "c" -or $User -eq "C") {
            $DomainDetails = Choose-Domain

            $AdminUser  = $DomainDetails[0]
            $Domain     = $DomainDetails[1]
            $DomainName = $DomainDetails[2]
        }
        Else{
            Write "Defaults to [1] Check status of [$User]
    [1] Check status of [$User]
    [2] Reset [$User] password
    [3] Unlock [$User] Account
    [4] Choose Domain again
    [5] Quit"
            
            $Choice = Read-Host -Prompt "What would you like to do?"
            $ChoiceArray = @("1", "2", "3", "4", "5", "q", "Q")
            
            If ($ChoiceArray -contains "$Choice") {
                Write "You chose option [$Choice]"
            }
            Else {
                Write "Defaulting to option [1]"
                $Choice = "1"
            }

            If ($Choice -eq "5" -or $Choice -eq "q" -or $Choice -eq "Q") {
                Write "Goodbye"
                $Done = $True
            }
            ElseIf ($Choice -eq "1") {
                 Get-ADUser -Identity $User -Server $Domain -Properties Name, LockedOut, Office, mobile, EmailAddress | Select-Object Name, LockedOut, Office, mobile, EmailAddress
            }
            ElseIf ($Choice -eq "2") {
                Reset-Pass $User $Domain $AdminUser #DON'T USE. Changing AD may cause weird things to happen. Everything is part of a ecosystem
            }
            ElseIf ($Choice -eq "3") {
                Check-Locked-Status $User $Domain $AdminUser
            }
            ElseIf ($Choice -eq "4") {
                $DomainDetails = Choose-Domain

                $AdminUser  = $DomainDetails[0]
                $Domain     = $DomainDetails[1]
                $DomainName = $DomainDetails[2]
            }
        }
    }
}

Main-Menu

