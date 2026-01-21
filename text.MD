# TikTok Video Upload - Test Cases

---

### Test Case TC_UPLOAD_000
**Title:** Allows MP4 File  
**Requirement:** Must allow MP4 file  
**Test Type:** Positive  

**Preconditions:**
- User is logged in
- Valid video file is available

**Test Steps:**
1. Attempt to upload a file

**Test Data:**
- MP4 file

**Expected Result:**
- Pass. MP4 files are allowed to be submitted

**Priority:** Medium

---

### Test Case TC_UPLOAD_001
**Title:** Allows 286MB File Size  
**Requirement:** Must allow 286MB file size  
**Test Type:** Positive  

**Preconditions:**
- User is logged in
- Valid video file is available

**Test Steps:**
1. Attempt to upload a file

**Test Data:**
- 286MB valid video file

**Expected Result:**
- Pass. Files of 286MB are allowed

**Priority:** Medium

---

### Test Case TC_UPLOAD_002
**Title:**  Prohibits JPG File  
**Requirement:** Must not allow JPG file  
**Test Type:** Negative  

**Preconditions:**
- User is logged in
- Valid image file is available

**Test Steps:**
1. Attempt to upload a file

**Test Data:**
- JPG file

**Expected Result:**
- Fail. JPG files are not allowed to be submitted

**Priority:** Medium

---

### Test Case TC_UPLOAD_003
**Title:** Prohibits Less Than 3 Seconds  
**Requirement:** Must not allow content shorter than 3 seconds  
**Test Type:** Negative  

**Preconditions:**
- User is logged in
- Valid video file is available

**Test Steps:**
1. Attempt to upload a file

**Test Data:**
- 2-second valid video file

**Expected Result:**
- Fail. Videos shorter than 3 seconds are not allowed

**Priority:** Medium

---

### Test Case TC_UPLOAD_004
**Title:**  Prohibits Empty Submission  
**Requirement:** Must not allow empty content  
**Test Type:** Edge Case  

**Preconditions:**
- User is logged in
- No video file selected

**Test Steps:**
1. Attempt to submit without selecting a file

**Test Data:**
- No file

**Expected Result:**
- Fail. A file is required to submit content

**Priority:** Medium

---

### Test Case TC_UPLOAD_005
**Title:** Allows 4-Second Video  
**Requirement:** Must allow 4-second content  
**Test Type:** Edge Case  

**Preconditions:**
- User is logged in
- Valid video file is available

**Test Steps:**
1. Attempt to upload a file

**Test Data:**
- 4-second valid video file

**Expected Result:**
- Pass. Videos of 4 seconds are allowed

**Priority:** Medium

---

### Test Case TC_UPLOAD_006
**Title:** Prohibits More Than 10-Minute Video  
**Requirement:** Must not allow videos longer than 10 minutes  
**Test Type:** Black Box  

**Preconditions:**
- User is logged in
- Valid video file is available

**Test Steps:**
1. Attempt to upload a file

**Test Data:**
- 11-minute valid video file

**Expected Result:**
- Fail. Videos longer than 10 minutes are not allowed

**Priority:** High

---

### Test Case TC_UPLOAD_007
**Title:** Prohibits 2,201 Character Caption  
**Requirement:** Must not allow captions longer than 2,200 characters  
**Test Type:** Black Box  

**Preconditions:**
- User is logged in

**Test Steps:**
1. Attempt to set a caption exceeding the character limit

**Test Data:**
- 2,201-character caption

**Expected Result:**
- Fail. Captions over 2,200 characters are not allowed

**Priority:** Medium

---

### Test Case TC_UPLOAD_008
**Title:** Allows 10-Minute Video  
**Requirement:** Must allow 10-minute content  
**Test Type:** Boundary  

**Preconditions:**
- User is logged in
- Valid video file is available

**Test Steps:**
1. Attempt to upload a file

**Test Data:**
- 10-minute valid video file

**Expected Result:**
- Pass. Videos of 10 minutes are allowed

**Priority:** Medium

---

### Test Case TC_UPLOAD_009
**Title:** Allows 3-Second Video  
**Requirement:** Must allow 3-second content  
**Test Type:** Boundary  

**Preconditions:**
- User is logged in
- Valid video file is available

**Test Steps:**
1. Attempt to upload a file

**Test Data:**
- 3-second valid video file

**Expected Result:**
- Pass. Videos of 3 seconds are allowed

**Priority:** Medium
