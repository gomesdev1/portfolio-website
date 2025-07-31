import { useState, useEffect, useCallback } from 'react';
import { portfolioAPI } from '../services/api';
import { mockData } from '../mock/data';

// Transform backend data to frontend format
const transformPortfolioData = (backendData) => {
  if (!backendData || !backendData.data) return null;

  const data = backendData.data;

  // Transform skills
  const transformedSkills = data.skills?.map(skill => ({
    category: skill.category?.pt || skill.category,
    technologies: skill.technologies || []
  })) || [];

  // Transform education
  const transformedEducation = data.education?.map(edu => ({
    institution: edu.institution,
    degree: edu.degree?.pt || edu.degree,
    period: edu.period,
    status: edu.status?.pt || edu.status
  })) || [];

  // Transform projects
  const transformedProjects = data.projects?.map(project => ({
    id: project.id || project._id,
    title: project.title?.pt || project.title || "EM DESENVOLVIMENTO",
    description: project.description?.pt || project.description || "Projetos serão adicionados conforme desenvolvimento",
    status: project.status || "placeholder",
    technologies: project.technologies || []
  })) || [];

  // Transform goals
  const transformedGoals = data.goals?.map(goal => 
    goal.goal?.pt || goal.goal
  ) || [];

  // Transform current learning
  const transformedCurrentLearning = data.current_learning?.map(item =>
    item.item?.pt || item.item
  ) || [];

  // Create multilingual structure compatible with existing frontend
  const portfolioData = {
    pt: {
      personalInfo: {
        name: data.personal_info?.name || "Pedro Gomes",
        title: data.personal_info?.title?.pt || "Desenvolvedor Fullstack Junior",
        subtitle: data.personal_info?.subtitle?.pt || "Estudante de Engenharia de Software",
        description: data.personal_info?.description?.pt || "Desenvolvedor em formação",
        location: data.personal_info?.location || "Brasil",
        status: data.personal_info?.status?.pt || "Disponível para estágio"
      },
      contact: {
        email: data.personal_info?.contact?.email || "pedroballario@gmail.com",
        linkedin: data.personal_info?.contact?.linkedin || "https://www.linkedin.com/in/pedro-gomes-ba4825354",
        github: data.personal_info?.contact?.github || "https://github.com/gomesdev1"
      },
      skills: transformedSkills,
      education: transformedEducation,
      projects: transformedProjects,
      goals: transformedGoals,
      currentLearning: transformedCurrentLearning,
      // Static navigation and sections (these don't change)
      navigation: {
        about: "SOBRE",
        skills: "HABILIDADES",
        projects: "PROJETOS", 
        contact: "CONTATO"
      },
      sections: {
        hero: {
          label: "DESENVOLVEDOR EM FORMAÇÃO",
          cta1: "ENTRAR EM CONTATO",
          cta2: "CONHECER MAIS"
        },
        about: {
          label: "QUEM SOU EU",
          title: "SOBRE",
          formationTitle: "FORMAÇÃO",
          goalsTitle: "OBJETIVOS"
        },
        skills: {
          label: "CONHECIMENTOS",
          title: "HABILIDADES",
          currentlyLearning: "ATUALMENTE ESTUDANDO"
        },
        projects: {
          label: "PORTFÓLIO",
          title: "PROJETOS",
          placeholder: "PROJETOS EM DESENVOLVIMENTO",
          placeholderDesc: "Esta seção será preenchida conforme novos projetos forem desenvolvidos durante meus estudos e práticas.",
          waitUpdate: "AGUARDE ATUALIZAÇÕES"
        },
        contact: {
          label: "VAMOS CONVERSAR",
          title: "CONTATO",
          description: "Estou em busca da minha primeira oportunidade de estágio para aplicar meus conhecimentos e continuar aprendendo.",
          availableFor: "DISPONÍVEL PARA",
          availability: [
            "• Estágio em Desenvolvimento",
            "• Projetos de Aprendizado",
            "• Mentorias", 
            "• Networking"
          ],
          sendEmail: "ENVIAR EMAIL",
          emailSubject: "Oportunidade de Estágio"
        }
      }
    },
    en: {
      personalInfo: {
        name: data.personal_info?.name || "Pedro Gomes",
        title: data.personal_info?.title?.en || "Junior Fullstack Developer",
        subtitle: data.personal_info?.subtitle?.en || "Software Engineering Student",
        description: data.personal_info?.description?.en || "Developer in training",
        location: data.personal_info?.location || "Brazil",
        status: data.personal_info?.status?.en || "Available for internship"
      },
      contact: {
        email: data.personal_info?.contact?.email || "pedro.gomes@exemplo.com",
        linkedin: data.personal_info?.contact?.linkedin || "https://linkedin.com/in/pedrogomes",
        github: data.personal_info?.contact?.github || "https://github.com/pedrogomes"
      },
      skills: data.skills?.map(skill => ({
        category: skill.category?.en || skill.category,
        technologies: skill.technologies || []
      })) || [],
      education: data.education?.map(edu => ({
        institution: edu.institution,
        degree: edu.degree?.en || edu.degree,
        period: edu.period,
        status: edu.status?.en || edu.status
      })) || [],
      projects: data.projects?.map(project => ({
        id: project.id || project._id,
        title: project.title?.en || project.title || "IN DEVELOPMENT",
        description: project.description?.en || project.description || "Projects will be added as development progresses",
        status: project.status || "placeholder",
        technologies: project.technologies || []
      })) || [],
      goals: data.goals?.map(goal => goal.goal?.en || goal.goal) || [],
      currentLearning: data.current_learning?.map(item => item.item?.en || item.item) || [],
      // Static navigation and sections in English
      navigation: {
        about: "ABOUT",
        skills: "SKILLS",
        projects: "PROJECTS",
        contact: "CONTACT"
      },
      sections: {
        hero: {
          label: "DEVELOPER IN TRAINING",
          cta1: "GET IN TOUCH",
          cta2: "LEARN MORE"
        },
        about: {
          label: "WHO I AM",
          title: "ABOUT", 
          formationTitle: "EDUCATION",
          goalsTitle: "GOALS"
        },
        skills: {
          label: "KNOWLEDGE",
          title: "SKILLS",
          currentlyLearning: "CURRENTLY LEARNING"
        },
        projects: {
          label: "PORTFOLIO",
          title: "PROJECTS",
          placeholder: "PROJECTS IN DEVELOPMENT",
          placeholderDesc: "This section will be filled as new projects are developed during my studies and practice.",
          waitUpdate: "AWAIT UPDATES"
        },
        contact: {
          label: "LET'S TALK",
          title: "CONTACT",
          description: "I'm looking for my first internship opportunity to apply my knowledge and continue learning.",
          availableFor: "AVAILABLE FOR",
          availability: [
            "• Development Internship",
            "• Learning Projects",
            "• Mentoring",
            "• Networking"
          ],
          sendEmail: "SEND EMAIL",
          emailSubject: "Internship Opportunity"
        }
      }
    }
  };

  return portfolioData;
};

export const usePortfolio = () => {
  const [portfolioData, setPortfolioData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [isOnline, setIsOnline] = useState(true);

  const fetchPortfolioData = useCallback(async () => {
    setLoading(true);
    setError(null);

    try {
      // First check if API is available
      const healthCheck = await portfolioAPI.healthCheck();
      
      if (!healthCheck.success) {
        console.warn('Backend not available, using mock data');
        setIsOnline(false);
        setPortfolioData(mockData);
        setLoading(false);
        return;
      }

      // Fetch portfolio data from backend
      const result = await portfolioAPI.getPortfolioData();
      
      if (result.success) {
        const transformedData = transformPortfolioData(result.data);
        if (transformedData) {
          setPortfolioData(transformedData);
          setIsOnline(true);
        } else {
          throw new Error('Failed to transform portfolio data');
        }
      } else {
        throw new Error(result.error || 'Failed to fetch portfolio data');
      }

    } catch (err) {
      console.error('Portfolio API Error:', err);
      console.warn('Falling back to mock data');
      
      // Fallback to mock data
      setError(err.message);
      setIsOnline(false);
      setPortfolioData(mockData);
    }

    setLoading(false);
  }, []);

  useEffect(() => {
    fetchPortfolioData();
  }, [fetchPortfolioData]);

  // Retry function for when backend comes back online
  const retry = useCallback(() => {
    fetchPortfolioData();
  }, [fetchPortfolioData]);

  return {
    portfolioData,
    loading,
    error,
    isOnline,
    retry,
    refetch: fetchPortfolioData
  };
};