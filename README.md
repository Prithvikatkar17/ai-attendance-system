# AI Attendance System 🤖📅

An AI-powered attendance system that uses **face recognition** and **voice recognition** to automatically detect and record student attendance in real-time. Built with a modern tech stack to ensure seamless, secure, and fast attendance tracking.

## 🚀 Features

- **Face Recognition**: Automatically identify students through webcam using state-of-the-art face recognition models (`dlib`, `face_recognition`).
- **Voice Recognition**: Adds an extra layer of biometric verification using voice analysis (`librosa`, `resemblyzer`).
- **Role-Based Access**: 
  - **Teacher Portal**: View class attendance, manage records, and initiate attendance sessions.
  - **Student Portal**: Check attendance status and history.
- **Real-Time Database**: Uses **Supabase** for fast, reliable, and secure data storage and retrieval.
- **Web Interface**: Clean, interactive UI built with **Streamlit**.

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend / Database**: Supabase (PostgreSQL)
- **AI & Biometrics**: 
  - Face Recognition (`dlib-bin`, `face-recognition`)
  - Voice Recognition (`librosa`, `resemblyzer`, `webrtcvad`)
  - ML utilities (`numpy`, `pandas`, `scikit-learn`, `torch`)
- **Other Tools**: `bcrypt` (security), `segno` (QR codes), `pillow` (image processing)

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Prithvikatkar17/ai-attendance-system.git
   cd ai-attendance-system
   ```

2. **Install dependencies:**
   Make sure you have `cmake` and `build-essential` installed on your system (required for building `dlib`).
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Supabase:**
   Configure your Supabase credentials. You may need to create a `.streamlit/secrets.toml` file to store your API keys and database URLs.

4. **Run the Application:**
   ```bash
   streamlit run app.py
   ```

## ☁️ Deployment

This project is configured for deployment on platforms like Streamlit Community Cloud. 
- The `packages.txt` file ensures system-level dependencies (`cmake`, `build-essential`) are installed in the cloud environment prior to installing Python packages.

## 📁 Project Structure

- `app.py`: Main application entry point and routing.
- `src/`: Core source code.
  - `components/`: Reusable Streamlit UI components.
  - `database/`: Supabase connection and database queries.
  - `pipelines/`: Face and voice recognition logic.
  - `screens/`: Teacher, student, and home screen views.
  - `ui/`: Additional UI styling and rendering logic.

## 📝 License
This project is open-source and available under the MIT License.
