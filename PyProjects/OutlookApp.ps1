<# Some constants with Outlook
CONST olAppointmentItem = 1
CONST olFolderDeletedItems = 3
CONST olFolderOutbox = 4
CONST olFolderSentMail = 5
CONST olFolderInbox = 6
CONST olFolderCalendar = 9
CONST olFolderContacts = 10
CONST olFolderJournal = 11
CONST olFolderNotes = 12
CONST olFolderTasks = 13
CONST olFolderDrafts = 16
#>

$outlook = new-object -comobject Outlook.Application
$namespace = $outlook.GetNameSpace("MAPI")
$inbox = $namespace.GetDefaultFolder(6)
$app = 'AHC04'
$inbox.items |
    Where-Object{
        $_.Unread -and $_.Subject -match $App
        } |
    Sort-Object ReceivedTime -Descending |
    Select-Object Subject.ReceivedTime.SenderName -First 1
        