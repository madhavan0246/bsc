# 🏃‍♂️ Sports Survey Application

A modern, mobile-first Next.js application for conducting sports surveys and providing AI-powered insights. This app helps understand why people quit sports and provides personalized recommendations.

## ✨ Features

### 🏠 **Modern Home Screen**
- Beautiful gradient background
- Card-based layout with hover effects
- Touch-friendly buttons with icons
- Professional mobile app design

### 📋 **Comprehensive Survey Form**
- **5 streamlined pages** (reduced from 11 for better UX)
- All original questions preserved and organized logically:
  - **Page 1**: Personal Information (Age, Gender, Status, Area)
  - **Page 2**: Sports Experience (Sports played, Duration, Level)
  - **Page 3**: Professional Aspirations (Consideration, Reasons for not continuing)
  - **Page 4**: Motivation & Support (What would encourage)
  - **Page 5**: Your Perspective (Open-ended question)
- Progress bar with smooth animations
- Modern form controls with hover states
- Responsive grid layouts

### 🤖 **AI Integration**
- **Gemini AI**: Personalized suggestions based on individual responses
- **K-means Clustering**: Cluster-based recommendations
- Real-time API integration with loading states
- Error handling and fallback content

### 📊 **Data-Driven Insights**
- **Real CSV Integration**: Uses actual survey data from your CSV file
- **Interactive Charts**: 
  - Age group distribution (pie chart)
  - Gender distribution (bar chart)
  - Top reasons for quitting (horizontal bar chart)
  - Most popular sports (bar chart)
- **Key Statistics Dashboard**: Summary metrics and insights
- **Live Data Updates**: Automatically reflects new survey submissions

### 💾 **CSV Data Management**
- **Automatic CSV Writing**: Form submissions are automatically appended to your CSV file
- **Real-time Insights**: Charts and statistics update with new data
- **Data Persistence**: All responses saved with timestamps and unique IDs

### 📱 **Mobile-First Design**
- Fully responsive design optimized for phones
- Touch-friendly interface with proper spacing
- Bottom navigation with 4 tabs
- Professional mobile app aesthetics
- Smooth animations and transitions

## 🚀 Quick Start

### 1. Install Dependencies
```bash
npm install
```

### 2. Configure Gemini AI (Optional)
Create a `.env.local` file in the root directory:
```bash
GEMINI_API_KEY=your_gemini_api_key_here
```
Get your API key from: https://makersuite.google.com/app/apikey

### 3. Run Development Server
```bash
npm run dev
```

### 4. Open Application
Navigate to `http://localhost:3000`

## 📁 Project Structure

```
src/
├── app/
│   ├── api/
│   │   ├── csv/
│   │   │   ├── read/route.ts          # Read CSV data
│   │   │   ├── write/route.ts         # Write to CSV
│   │   │   └── insights/route.ts      # Generate insights from CSV
│   │   ├── gemini/route.ts            # Gemini AI integration
│   │   └── kmeans/route.ts            # K-means clustering
│   ├── layout.tsx                     # Root layout
│   ├── page.tsx                       # Main application
│   └── globals.css                    # Global styles
```

## 🔧 Key Improvements Made

### **Form Optimization**
- ✅ Reduced from 11 pages to 5 pages for better UX
- ✅ Grouped related questions logically
- ✅ Removed empty/question-less pages
- ✅ Added progress indicators and smooth navigation

### **UI/UX Enhancements**
- ✅ Modern gradient backgrounds and card layouts
- ✅ Professional mobile app design
- ✅ Touch-friendly buttons and form controls
- ✅ Smooth animations and hover effects
- ✅ Consistent color scheme and typography
- ✅ Loading states and error handling

### **CSV Integration**
- ✅ Automatic form submission to CSV file
- ✅ Real-time data analysis and insights
- ✅ Proper data formatting matching existing CSV structure
- ✅ Timestamp and unique ID generation

### **Data Visualization**
- ✅ Interactive charts using Recharts
- ✅ Real data from CSV file
- ✅ Multiple chart types (pie, bar, horizontal bar)
- ✅ Responsive chart sizing
- ✅ Color-coded data representation

## 📊 CSV Data Structure

The application automatically appends survey responses to your CSV file with the following structure:

```csv
Timestamp,Username,Age Group,Gender,Current Status,Area,Sports Played,Duration,Level,Professional Consideration,Reasons for Not Continuing,What Would Encourage,Biggest Reason
```

## 🎨 Design System

### **Colors**
- **Primary**: Purple (#8B5CF6) - Main actions and branding
- **Secondary**: Blue (#3B82F6) - AI-related content
- **Success**: Green (#10B981) - K-means and positive actions
- **Warning**: Orange (#F59E0B) - Sports-related content
- **Background**: Gradient from purple-50 to blue-50

### **Typography**
- **Headings**: Bold, large sizes for hierarchy
- **Body**: Medium weight, good contrast
- **Captions**: Smaller, muted colors

### **Components**
- **Cards**: Rounded corners (2xl), shadows, hover effects
- **Buttons**: Gradient backgrounds, rounded corners, hover states
- **Forms**: Border styling, focus states, validation
- **Navigation**: Bottom tab bar with active states

## 🔌 API Endpoints

### **CSV Operations**
- `GET /api/csv/read` - Read all CSV data
- `POST /api/csv/write` - Write new survey response
- `GET /api/csv/insights` - Generate insights from CSV data

### **AI Integration**
- `POST /api/gemini` - Get AI suggestions (personal/overall)
- `POST /api/kmeans` - Get cluster-based suggestions

## 📱 Mobile Responsiveness

The application is fully optimized for mobile devices:
- Touch targets are at least 44px
- Proper spacing for thumb navigation
- Responsive charts that adapt to screen size
- Bottom navigation for easy access
- Optimized typography for mobile reading

## 🚀 Deployment

### **Vercel (Recommended)**
1. Push code to GitHub
2. Connect repository to Vercel
3. Add environment variables in Vercel dashboard
4. Deploy automatically

### **Other Platforms**
- Build: `npm run build`
- Start: `npm start`
- Ensure environment variables are set in production

## 🔧 Configuration

### **Environment Variables**
- `GEMINI_API_KEY` (optional): Your Google Gemini AI API key

### **CSV File Path**
The application expects your CSV file at:
```
C:\Users\Madhavan\Documents\bsc\backend\Barriers to Continuing Sports .csv
```

## 📈 Analytics & Insights

The insights page provides:
- **Demographic Analysis**: Age groups, gender, location distribution
- **Sports Analysis**: Most popular sports, participation levels
- **Barrier Analysis**: Top reasons people quit sports
- **Trend Analysis**: Participation patterns and career considerations
- **Key Statistics**: Summary metrics and insights

## 🛠️ Customization

### **Adding New Questions**
1. Update the `formData` state in `SurveyForm`
2. Add new case in `renderPage()` function
3. Update the `totalPages` constant if needed
4. Add form fields in the appropriate page case

### **Modifying Charts**
- Update data processing in `/api/csv/insights/route.ts`
- Customize colors and styling in the insights components
- Add new chart types using Recharts

### **Styling Changes**
- All styling uses Tailwind CSS
- Colors and gradients can be customized in the components
- Consistent design system throughout the app

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly on mobile devices
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🎯 Next Steps

- [ ] Add data export functionality
- [ ] Implement user authentication
- [ ] Add survey analytics dashboard
- [ ] Create admin panel for data management
- [ ] Add email notifications for survey completion
- [ ] Implement survey sharing functionality

---

**Built with ❤️ using Next.js, TypeScript, Tailwind CSS, and Recharts**