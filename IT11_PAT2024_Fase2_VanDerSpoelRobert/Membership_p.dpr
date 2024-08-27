program Membership_p;

uses
  Vcl.Forms,
  RobertPATmain_u in 'RobertPATmain_u.pas' {frmMain};

{$R *.res}

begin
  Application.Initialize;
  Application.MainFormOnTaskbar := True;
  Application.CreateForm(TfrmMain, frmMain);
  Application.Run;
end.
