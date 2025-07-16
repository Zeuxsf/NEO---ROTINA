[Setup]
AppName=NeoTrax
AppVersion=1.0
DefaultDirName={autopf}\NeoTrax
DefaultGroupName=NeoTrax
UninstallDisplayIcon={app}\NeoTrax.exe
OutputDir=instalador
OutputBaseFilename=NeoTrax_Installer
Compression=lzma
SolidCompression=yes
SetupIconFile=dist\NeoTrax\_internal\imagens\ntx_logo.ico
ArchitecturesInstallIn64BitMode=x64

[Languages]
Name: "brazilianportuguese"; MessagesFile: "compiler:Languages\BrazilianPortuguese.isl"

[Files]
Source: "dist\NeoTrax\*"; DestDir: "{app}"; Flags: recursesubdirs createallsubdirs

[Icons]
Name: "{group}\NeoTrax"; Filename: "{app}\NeoTrax.exe"
Name: "{commondesktop}\NeoTrax"; Filename: "{app}\NeoTrax.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Criar atalho na Área de Trabalho"; GroupDescription: "Opções adicionais"; Flags: unchecked

[Run]
Filename: "{app}\NeoTrax.exe"; Description: "Executar NeoTrax agora"; Flags: nowait postinstall skipifsilent