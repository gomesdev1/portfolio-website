import axios from 'axios';

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API_BASE = `${BACKEND_URL}/api`;

// Create axios instance with default config
const apiClient = axios.create({
  baseURL: API_BASE,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add request interceptor for logging
apiClient.interceptors.request.use(
  (config) => {
    console.log(`API Request: ${config.method?.toUpperCase()} ${config.url}`);
    return config;
  },
  (error) => {
    console.error('API Request Error:', error);
    return Promise.reject(error);
  }
);

// Add response interceptor for error handling
apiClient.interceptors.response.use(
  (response) => {
    console.log(`API Response: ${response.status} ${response.config.url}`);
    return response;
  },
  (error) => {
    console.error('API Response Error:', error.response?.status, error.response?.data || error.message);
    return Promise.reject(error);
  }
);

// API service functions
export const portfolioAPI = {
  // Health check
  healthCheck: async () => {
    try {
      const response = await apiClient.get('/health');
      return { success: true, data: response.data };
    } catch (error) {
      return { success: false, error: error.message };
    }
  },

  // Get all portfolio data in one call
  getPortfolioData: async () => {
    try {
      const response = await apiClient.get('/portfolio');
      return { success: true, data: response.data };
    } catch (error) {
      return { success: false, error: error.message };
    }
  },

  // Personal Info
  getPersonalInfo: async () => {
    try {
      const response = await apiClient.get('/personal-info');
      return { success: true, data: response.data };
    } catch (error) {
      return { success: false, error: error.message };
    }
  },

  updatePersonalInfo: async (personalInfo) => {
    try {
      const response = await apiClient.put('/personal-info', personalInfo);
      return { success: true, data: response.data };
    } catch (error) {
      return { success: false, error: error.message };
    }
  },

  // Skills
  getSkills: async () => {
    try {
      const response = await apiClient.get('/skills');
      return { success: true, data: response.data };
    } catch (error) {
      return { success: false, error: error.message };
    }
  },

  createSkill: async (skillData) => {
    try {
      const response = await apiClient.post('/skills', skillData);
      return { success: true, data: response.data };
    } catch (error) {
      return { success: false, error: error.message };
    }
  },

  updateSkill: async (skillId, skillData) => {
    try {
      const response = await apiClient.put(`/skills/${skillId}`, skillData);
      return { success: true, data: response.data };
    } catch (error) {
      return { success: false, error: error.message };
    }
  },

  deleteSkill: async (skillId) => {
    try {
      const response = await apiClient.delete(`/skills/${skillId}`);
      return { success: true, data: response.data };
    } catch (error) {
      return { success: false, error: error.message };
    }
  },

  // Education
  getEducation: async () => {
    try {
      const response = await apiClient.get('/education');
      return { success: true, data: response.data };
    } catch (error) {
      return { success: false, error: error.message };
    }
  },

  createEducation: async (educationData) => {
    try {
      const response = await apiClient.post('/education', educationData);
      return { success: true, data: response.data };
    } catch (error) {
      return { success: false, error: error.message };
    }
  },

  // Projects
  getProjects: async () => {
    try {
      const response = await apiClient.get('/projects');
      return { success: true, data: response.data };
    } catch (error) {
      return { success: false, error: error.message };
    }
  },

  getFeaturedProjects: async () => {
    try {
      const response = await apiClient.get('/projects/featured');
      return { success: true, data: response.data };
    } catch (error) {
      return { success: false, error: error.message };
    }
  },

  createProject: async (projectData) => {
    try {
      const response = await apiClient.post('/projects', projectData);
      return { success: true, data: response.data };
    } catch (error) {
      return { success: false, error: error.message };
    }
  },

  updateProject: async (projectId, projectData) => {
    try {
      const response = await apiClient.put(`/projects/${projectId}`, projectData);
      return { success: true, data: response.data };
    } catch (error) {
      return { success: false, error: error.message };
    }
  },

  deleteProject: async (projectId) => {
    try {
      const response = await apiClient.delete(`/projects/${projectId}`);
      return { success: true, data: response.data };
    } catch (error) {
      return { success: false, error: error.message };
    }
  },

  // Goals
  getGoals: async () => {
    try {
      const response = await apiClient.get('/goals');
      return { success: true, data: response.data };
    } catch (error) {
      return { success: false, error: error.message };
    }
  },

  createGoal: async (goalData) => {
    try {
      const response = await apiClient.post('/goals', goalData);
      return { success: true, data: response.data };
    } catch (error) {
      return { success: false, error: error.message };
    }
  },

  // Current Learning
  getCurrentLearning: async () => {
    try {
      const response = await apiClient.get('/current-learning');
      return { success: true, data: response.data };
    } catch (error) {
      return { success: false, error: error.message };
    }
  },

  createCurrentLearning: async (learningData) => {
    try {
      const response = await apiClient.post('/current-learning', learningData);
      return { success: true, data: response.data };
    } catch (error) {
      return { success: false, error: error.message };
    }
  }
};

export default portfolioAPI;