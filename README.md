# CT Review Tool - AWS App Runner Deployment

## 🚀 Quick Deploy to AWS App Runner

### Prerequisites
- AWS Account with App Runner access
- GitHub repository (public or connected private)

### Deployment Steps

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/ct-review-tool.git
   git push -u origin main
   ```

2. **Create App Runner Service**
   - Go to AWS App Runner console
   - Click "Create service"
   - Choose "Source code repository"
   - Connect your GitHub repository
   - Select this repository and branch
   - App Runner will auto-detect the `apprunner.yaml` configuration

3. **Service Configuration**
   - Service name: `ct-review-tool`
   - Port: `8080` (auto-configured)
   - Health check: `/` (default)

### Files Structure
```
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── apprunner.yaml     # App Runner configuration
├── core_functionality.py  # Business logic
├── ui_components.py       # UI components
└── Writeup_AI_V4_29_10.txt # Original code
```

### Features
- ✅ Document upload (.docx)
- ✅ Section-by-section analysis
- ✅ AI feedback generation
- ✅ Accept/reject feedback
- ✅ Download reviewed document
- ✅ Responsive web interface

### Usage
1. Upload a .docx document
2. Select sections to analyze
3. Review AI-generated feedback
4. Accept or reject suggestions
5. Download enhanced document

### Cost Estimation
- AWS App Runner: ~$25-50/month for basic usage
- Scales automatically based on traffic
- Pay only for active usage time

### Environment Variables
- `PORT`: 8080 (auto-configured by App Runner)

### Monitoring
- App Runner provides built-in logs and metrics
- Access via AWS Console > App Runner > Your Service > Logs