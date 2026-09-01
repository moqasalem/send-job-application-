function sendJobApplications() {
  const MAX_EMAILS = 100;

  const sheet = SpreadsheetApp.getActiveSpreadsheet()
    .getSheetByName("Sheet1");

  const cvFileId = "YOUR_GOOGLE_DRIVE_FILE_ID";
  const cvFile = DriveApp.getFileById(cvFileId);

  const data = sheet.getDataRange().getValues();

  let sentCount = 0;

  for (let i = 1; i < data.length; i++) {

    // Stop after reaching the limit
    if (sentCount >= MAX_EMAILS) {
      break;
    }

    const company = data[i][0];
    const email = data[i][1];
    const status = data[i][2];

    if (!email || !company) {
      continue;
    }

    if (status === "SENT") {
      continue;
    }

    const subject =
      "Backend / Full-Stack Developer – Salem Moqa – CV";

    const body = `
Dear ${company} Recruitment Team,

I am writing to express my interest in Backend / Full-Stack
Developer opportunities at ${company}.

I have 6 years of experience in backend development, with
experience in Laravel, PHP, MySQL, Node.js, and web development.

Please find my CV attached for your consideration.

I would be pleased to discuss any suitable opportunities
within your organization.

Best regards,
Salem Moqa
`;

    try {
      GmailApp.sendEmail(email, subject, body, {
        attachments: [cvFile.getBlob()],
        name: "Salem Moqa"
      });

      sheet.getRange(i + 1, 3).setValue("SENT");

      sentCount++;

    } catch (error) {
      sheet.getRange(i + 1, 3)
        .setValue("ERROR: " + error.message);
    }
  }

  Logger.log(`Sent ${sentCount} emails.`);
}
