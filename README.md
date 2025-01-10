# SkillSync Project README

## Overview

SkillSync is a Python-based Command-Line Interface (CLI) application that helps users manage workshop bookings and one-on-one meetings with mentors and peers. It uses Firebase for authentication and database management, while integrating with the Google Calendar API for scheduling meetings. This terminal-based application ensures all meetings occur strictly on weekdays between 07:00 and 17:00.

## Features

### 1. **Authentication**
- **Purpose**: Secure user access to the system.
- **Implementation**: Firebase Authentication for login and sign-up functionality.
- **Database Integration**:
  - Stores user details (name, email, role).
  - Maintains user roles (mentor/peer).

### 2. **Booking System**
- **Mentor Sessions**:
  - Fetch and display a list of available mentors.
  - Request meetings with selected mentors.
- **Peer Sessions**:
  - Search for peers by availability or expertise.
  - Schedule one-on-one meetings.

### 3. **Google Calendar Integration**
- **Purpose**: Ensure meeting schedules are visible and manageable.
- **Features**:
  - Create calendar events for confirmed bookings.
  - Automatically send calendar invites to all participants.
  - Ensure meetings are strictly scheduled during weekdays (Monday to Friday) between 07:00 and 17:00.

### 4. **CLI Functionality**
Developed using the `click` library to provide a user-friendly terminal interface. Key menu options include:
- **Login**: Authenticate users.
- **View Workshops**: List upcoming workshops and mentors available for booking.
- **Request Meeting**: Request a mentor or peer session.
- **View Bookings**: Display a list of all confirmed bookings.
- **Cancel Booking**: Allow users to cancel an existing booking.

### 5. **Database Structure**
- **Users**: 
  - `user_id`: { `name`, `email`, `role (mentor/peer)`, `expertise` }
- **Meetings**: 
  - `meeting_id`: { `mentor_id`, `mentee_id/peer_id`, `time`, `status` }
- **Workshop Requests**: 
  - `workshop_id`: { `requestor_id`, `topic`, `date_requested` }

## Technical Requirements

### 1. **Tools and Frameworks**
- **Firebase**: For authentication and database management.
- **Google Calendar API**: For scheduling and managing meetings.
- **Python Libraries**:
  - `click`: CLI framework.
  - `firebase-admin`: Firebase integration.
  - `google-api-python-client`: Google Calendar API integration.
- **pyinstaller**: For packaging the application into a distributable executable.

### 2. **Meeting Time Constraints**
- All meetings must occur strictly on weekdays (Monday to Friday) between 07:00 and 17:00.
- Developers must enforce and represent this scheduling constraint within both the database and the application logic.

### 3. **Stretch Features (Optional)**
- **Email Notifications**: Notify users about meeting confirmations and reminders using SMTP (via `smtplib`).
- **Feedback System**: Allow users to rate and leave feedback for mentors and peers.
- **Search Filters**: Enable filtering mentors and peers by expertise or availability.

## Packaging and Distribution

- The application will be packaged using **pyinstaller** to generate a distributable executable for various operating systems (Windows, macOS, Linux).

## Next Steps

1. **Set up Firebase**:
   - Configure Firebase Authentication and Firestore database.
   
2. **Integrate Google Calendar API**:
   - Enable event creation and manage participants.
   
3. **Develop the CLI**:
   - Use the `click` library to implement interactive terminal commands.
   
4. **Test and Package**:
   - Validate the features.
   - Package the application using `pyinstaller` for distribution.

## Installation Instructions

### Prerequisites:
1. Install Python (version 3.6 or above).
2. Set up Firebase project and obtain credentials for Firebase Authentication and Firestore.
3. Set up Google Cloud Project and enable Google Calendar API.

### Setup:
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repository/skillsync.git
   cd skillsync
