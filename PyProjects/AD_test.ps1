Import-Module ActiveDirectory

function Check-Locked-Status($User, $Domain, $AdminUser) #works. NEED ADMIN
{
    #Checks if locked out or not
    $IsLockedOut = Get-ADUser -Identity "$User" -Server "$Domain" -Properties LockedOut | Select -Expand LockedOut
    If ($IsLockedOut) {
        Write "Unlocking account..."
        Unlock-ADAccount -Identity $User -Server $Domain -Credential ($DomainName + $AdminUser)
    }
    Else{
        Write "$User is NOT locked out. Goodbye"
    } 
}

function Reset-Pass($User, $Domain) #NEED ADMIN
{
    #HOPEFULLY resets password. I need a test account or someone willing to play along

}

function Change-Phone($User, $Domain) #No need for admin
{
    #Gets, confirms and changes mobile number!
    $Mobile = Get-ADUser -Identity "$User" -Server "$Domain" -Properties mobile | Select -Expand mobile
    Write-Host "Current mobile number is: $Mobile"
    
    $ReallyChange = Read-Host -Prompt "You sure you want to change ${Mobile}? Y/N"
    If($ReallyChange -eq "Y" -or $ReallyChange -eq "y")
    {
        $NewMobile = Read-Host -Prompt "Please enter new number"
        Set-ADUser -Identity "$User" -Server "$Domain" -mobile $NewMobile
    }
    Else{
        Write "Mobile number not changed"
    }
}

function Change-Address($User, $Domain) #No need for admin
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
        Set-ADUser -Identity "$User" -Server "$Domain" -StreetAddress $Street -City $City -PostalCode $Postal
    }
    Else{
        Write "Address not changed"
    }
}

$User = Read-Host -Prompt "Please enter the username"
$Domain = Read-Host -Prompt "[1] RIMNET/BlackBerry
[2] SPRINGTHINGS/Good Tech
Please choose the domain number you wish to access"

If($Domain -eq "1") {
    $Domain = "rim.net"
}
ElseIf($Domain -eq "2") {
    $Domain = "corp.good.com"
}
Else {
    Write "Invalide choice"
}
#Check-Locked-Status $User $Domain #to call a function, arguments are separated by spaces!
#Change-Address $User $Domain
Change-Phone $User $Domain