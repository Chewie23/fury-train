function Choose-Domain(){
    $Domain = Read-Host -Prompt "Defaults to BlackBerry RIMNET
    [1] BlackBerry RIMNET
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
    $AdminUser = Read-Host -Prompt "Please enter your admin username"
    
    $AdminUser 
    $Domain
    $DomainName
    return
}

$DomainDetails = Choose-Domain

$AdminUser  = $DomainDetails[0]
$Domain     = $DomainDetails[1]
$DomainName = $DomainDetails[2]