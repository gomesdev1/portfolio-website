// Mock data para o portfolio - Multilingual
export const mockData = {
  pt: {
    personalInfo: {
      name: "Pedro Gomes",
      title: "Desenvolvedor Fullstack Junior",
      subtitle: "Estudante de Engenharia de Software",
      description: "Cursando Bacharelado em Engenharia de Software (1º semestre) na Universidade Anhaguera, com formação técnica em suporte de TI. Focado em Java, Spring Boot e tecnologias modernas.",
      location: "Brasil",
      status: "Disponível para estágio"
    },
    
    contact: {
      email: "pedro.gomes@exemplo.com",
      linkedin: "https://linkedin.com/in/pedrogomes",
      github: "https://github.com/pedrogomes"
    },
    
    skills: [
      {
        category: "Backend",
        technologies: ["Java", "Spring Boot", "MongoDB", "APIs REST", "Orientação a Objetos"]
      },
      {
        category: "Frontend", 
        technologies: ["HTML", "CSS", "JavaScript", "React (aprendendo)"]
      },
      {
        category: "Ferramentas",
        technologies: ["Git", "Linux", "Suporte Técnico", "Redes de Computadores"]
      },
      {
        category: "Soft Skills",
        technologies: ["Autodidata", "Dedicado", "Foco em Aprendizado", "Orientado a Detalhes"]
      }
    ],
    
    education: [
      {
        institution: "Universidade Anhaguera",
        degree: "Bacharelado em Engenharia de Software",
        period: "2024 - Em andamento",
        status: "1º Semestre"
      },
      {
        institution: "Formação Técnica",
        degree: "Suporte de TI",
        period: "Concluído",
        status: "Redes, Hardware, Software"
      }
    ],
    
    currentLearning: [
      "Curso Java com Spring Boot",
      "Desenvolvimento de APIs",
      "MongoDB e NoSQL",
      "Frontend com React",
      "Boas práticas de desenvolvimento"
    ],
    
    projects: [
      {
        id: 1,
        title: "EM DESENVOLVIMENTO",
        description: "Projetos serão adicionados conforme desenvolvimento",
        status: "placeholder",
        technologies: []
      }
    ],
    
    goals: [
      "Conquistar primeira oportunidade de estágio",
      "Evoluir como desenvolvedor de software", 
      "Tornar-se engenheiro de software",
      "Dominar tecnologias fullstack"
    ],

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
      name: "Pedro Gomes",
      title: "Junior Fullstack Developer",
      subtitle: "Software Engineering Student",
      description: "Currently pursuing a Bachelor's degree in Software Engineering (1st semester) at Anhaguera University, with technical background in IT support. Focused on Java, Spring Boot and modern technologies.",
      location: "Brazil",
      status: "Available for internship"
    },
    
    contact: {
      email: "pedro.gomes@exemplo.com",
      linkedin: "https://linkedin.com/in/pedrogomes",
      github: "https://github.com/pedrogomes"
    },
    
    skills: [
      {
        category: "Backend",
        technologies: ["Java", "Spring Boot", "MongoDB", "REST APIs", "Object Oriented Programming"]
      },
      {
        category: "Frontend", 
        technologies: ["HTML", "CSS", "JavaScript", "React (learning)"]
      },
      {
        category: "Tools",
        technologies: ["Git", "Linux", "Technical Support", "Computer Networks"]
      },
      {
        category: "Soft Skills",
        technologies: ["Self-taught", "Dedicated", "Learning Focused", "Detail Oriented"]
      }
    ],
    
    education: [
      {
        institution: "Anhaguera University",
        degree: "Bachelor's in Software Engineering",
        period: "2024 - In progress",
        status: "1st Semester"
      },
      {
        institution: "Technical Training",
        degree: "IT Support",
        period: "Completed",
        status: "Networks, Hardware, Software"
      }
    ],
    
    currentLearning: [
      "Java course with Spring Boot",
      "API Development",
      "MongoDB and NoSQL",
      "Frontend with React",
      "Development best practices"
    ],
    
    projects: [
      {
        id: 1,
        title: "IN DEVELOPMENT",
        description: "Projects will be added as development progresses",
        status: "placeholder",
        technologies: []
      }
    ],
    
    goals: [
      "Secure first internship opportunity",
      "Evolve as a software developer", 
      "Become a software engineer",
      "Master fullstack technologies"
    ],

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