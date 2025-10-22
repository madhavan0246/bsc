# Sports Survey Application Setup

## Overview
This is a Next.js application for conducting sports surveys and providing AI-powered insights. The app includes:

- **Home Screen**: Landing page with "Take Survey" and "View Insights" buttons
- **Survey Form**: Comprehensive 8-page survey with all specified questions
- **Results Page**: Shows personalized suggestions from both Gemini AI and K-means clustering
- **Insights Page**: Data visualizations with charts and overall recommendations
- **AI Suggestions Page**: Dedicated page for overall AI insights and recommendations

## Features

### Survey Questions Included:
1. Age group selection
2. Gender identification
3. Current status (School/College/Working)
4. Area type (Urban/Semi-urban/Rural)
5. Sports played (multiple selection)
6. Duration of sports participation
7. Level of sports participation
8. Consideration of professional sports
9. Reasons for not continuing professionally
10. What would encourage continued participation
11. Open-ended question about biggest reasons people quit sports

### AI Integration:
- **Gemini AI**: Provides personalized suggestions based on individual responses
- **K-means Clustering**: Simulates cluster-based recommendations (ready for backend integration)
- **Overall Insights**: AI-generated community-level recommendations

### Data Visualizations:
- Age group distribution (pie chart)
- Demographic distribution (bar chart)
- Reasons for quitting (horizontal bar chart)

## Setup Instructions

### 1. Install Dependencies
```bash
npm install
```

### 2. Configure Gemini AI API Key
Create a `.env.local` file in the root directory:
```bash
GEMINI_API_KEY=your_gemini_api_key_here
```

Get your API key from: https://makersuite.google.com/app/apikey

### 3. Run the Development Server
```bash
npm run dev
```

The application will be available at `http://localhost:3000`

## Project Structure

```
src/
├── app/
│   ├── api/
│   │   ├── gemini/
│   │   │   └── route.ts          # Gemini AI API integration
│   │   └── kmeans/
│   │       └── route.ts          # K-means clustering API
│   ├── layout.tsx                # Root layout
│   ├── page.tsx                  # Main application component
│   └── globals.css               # Global styles
```

## Key Components

### HomePage
- Main component managing navigation between different pages
- Bottom navigation bar with 4 tabs: Home, Survey, Insights, AI Suggestions

### SurveyForm
- Multi-page form with progress indicator
- Handles all survey questions with proper validation
- Submits data to both Gemini and K-means APIs

### ResultsPage
- Displays personalized suggestions from both AI systems
- Shows loading states during API calls
- Provides navigation back to survey or insights

### InsightsPage
- Data visualizations using Recharts
- Overall AI insights and recommendations
- Download report functionality

### AISuggestionsPage
- Dedicated page for AI-generated insights
- Recommended solutions for the sports community
- Download report functionality

## Mobile Responsiveness

The application is fully responsive and optimized for mobile devices:
- Touch-friendly buttons and form elements
- Proper spacing and typography for mobile screens
- Bottom navigation bar for easy thumb navigation
- Responsive charts that adapt to screen size

## API Integration

### Gemini AI API
- Personal suggestions based on individual survey responses
- Overall insights for the community
- Handles both success and error states

### K-means API
- Currently simulated with predefined logic
- Ready for integration with your backend API
- Cluster-based recommendations

## Customization

### Adding New Survey Questions
1. Update the `formData` state in `SurveyForm`
2. Add new case in `renderPage()` function
3. Update the `totalPages` constant
4. Add form fields in the appropriate page case

### Modifying Charts
- Update data arrays in `InsightsPage` component
- Customize colors and styling
- Add new chart types using Recharts

### Styling Changes
- All styling uses Tailwind CSS
- Color scheme: Purple (#8B5CF6) for primary actions, Blue (#3B82F6) for AI, Green (#10B981) for K-means
- Consistent card-based layout with rounded corners and shadows

## Deployment

### Vercel (Recommended)
1. Push code to GitHub
2. Connect repository to Vercel
3. Add environment variables in Vercel dashboard
4. Deploy automatically

### Other Platforms
- Build: `npm run build`
- Start: `npm start`
- Ensure environment variables are set in production

## Environment Variables

Required:
- `GEMINI_API_KEY`: Your Google Gemini AI API key

Optional:
- Any additional API keys for K-means backend integration

## Browser Support

- Modern browsers (Chrome, Firefox, Safari, Edge)
- Mobile browsers (iOS Safari, Chrome Mobile)
- Responsive design works on all screen sizes

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

