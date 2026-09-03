# Send Job Applications

A simple Google Apps Script that helps automate sending job applications from a Google Sheet.

The script reads company names and email addresses from a spreadsheet, sends a predefined job application email with a CV attachment, and updates the application status after sending.

## Features

* 📧 Send job applications automatically
* 📎 Attach your CV from Google Drive
* 📊 Read company information from Google Sheets
* ✅ Mark successfully sent applications as `SENT`
* ❌ Record errors directly in the spreadsheet
* 🔢 Set a maximum number of emails per execution

## Google Sheet Format

The script expects a sheet named `Sheet1` with the following columns:

| Company   | Email                                             | Status |
| --------- | ------------------------------------------------- | ------ |
| Company A | [careers@company.com](mailto:careers@company.com) |        |
| Company B | [jobs@company.com](mailto:jobs@company.com)       | SENT   |

The script skips:

* Rows without a company or email
* Applications already marked as `SENT`

## Setup

1. Create a Google Sheet.
2. Create a sheet named `Sheet1`.
3. Add the following columns:

```text
Company | Email | Status
```

4. Upload your CV to Google Drive.
5. Copy the CV file ID.
6. Replace the `cvFileId` value in the script:

```javascript
const cvFileId = "YOUR_GOOGLE_DRIVE_FILE_ID";
```
7. Edit the subject and body of the email using your own words. 
8. Open **Extensions → Apps Script** in Google Sheets.
9. Add the script.
10. Run `sendJobApplications()`.
11. Grant the required Google account permissions when prompted.

## Configuration

You can control the maximum number of emails sent in each execution:

```javascript
const MAX_EMAILS = 10;
```

For example:

```javascript
const MAX_EMAILS = 20;
```

## How It Works

```text
Google Sheet
     ↓
Read company & email
     ↓
Skip SENT rows
     ↓
Create email
     ↓
Attach CV
     ↓
Send email
     ↓
Update Status → SENT
```

If sending fails, the script stores the error in the `Status` column.

## Important

This project is intended for personal job-search automation.

Make sure your use complies with Google's email sending limits[100 emails using google script] and the policies of the email service you are using. Avoid sending unsolicited or excessive emails.

## License

MIT
