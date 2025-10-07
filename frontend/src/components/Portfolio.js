import React, { useState, useEffect } from 'react';
import { Mail, Github, Linkedin, MapPin, Target, User, Briefcase, Code, GraduationCap, Sun, Moon, Globe } from 'lucide-react';
import { usePortfolio } from '../../public/Portfolio';
import LoadingSpinner from './LoadingSpinner';
import ErrorMessage from './ErrorBoundary';

const Portfolio = () => {
  const [activeSection, setActiveSection] = useState('sobre');
  const [language, setLanguage] = useState('pt');
  const [theme, setTheme] = useState('dark');
  const [showError, setShowError] = useState(true);

  const { portfolioData, loading, error, isOnline, retry } = usePortfolio();

  // Initialize theme on component mount
  useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme);
  }, [theme]);

  // Auto-hide error message after 10 seconds
  useEffect(() => {
    if (error && !isOnline) {
      const timer = setTimeout(() => {
        setShowError(false);
      }, 10000);
      return () => clearTimeout(timer);
    }
  }, [error, isOnline]);

  const toggleTheme = () => {
    const newTheme = theme === 'light' ? 'dark' : 'light';
    setTheme(newTheme);
    document.documentElement.setAttribute('data-theme', newTheme);
  };

  const toggleLanguage = () => {
    setLanguage(language === 'pt' ? 'en' : 'pt');
  };

  const scrollToSection = (sectionId) => {
    const element = document.getElementById(sectionId);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
      setActiveSection(sectionId);
    }
  };

  // Show loading spinner while fetching data
  if (loading) {
    return <LoadingSpinner message={language === 'pt' ? 'Carregando portfolio...' : 'Loading portfolio...'} />;
  }

  // Show error if no data is available
  if (!portfolioData) {
    return (
      <div className="error-fallback">
        <h2>Erro ao carregar portfolio</h2>
        <button onClick={retry} className="btn-accent">Tentar Novamente</button>
      </div>
    );
  }

  const currentData = portfolioData[language];

  return (
    <div className="portfolio">
      {/* Grid Background */}
      <div className="grid-background"></div>
      
      {/* Error Message (if backend is offline) */}
      {error && !isOnline && showError && (
        <ErrorMessage 
          error={error} 
          isOnline={isOnline} 
          onRetry={retry}
        />
      )}
      
      {/* Header */}
      <header className="header">
        <div className="container">
          <nav className="nav">
            <div className="header-logo">@GomesDev1</div>
            <div className="nav-controls">
              <div className="nav-menu">
                <a href="#sobre" className="nav-link" onClick={(e) => { e.preventDefault(); scrollToSection('sobre'); }}>
                  {currentData.navigation.about}
                </a>
                <a href="#habilidades" className="nav-link" onClick={(e) => { e.preventDefault(); scrollToSection('habilidades'); }}>
                  {currentData.navigation.skills}
                </a>
                <a href="#projetos" className="nav-link" onClick={(e) => { e.preventDefault(); scrollToSection('projetos'); }}>
                  {currentData.navigation.projects}
                </a>
                <a href="#contato" className="nav-link" onClick={(e) => { e.preventDefault(); scrollToSection('contato'); }}>
                  {currentData.navigation.contact}
                </a>
              </div>
              <div className="nav-toggles">
                <button 
                  className="btn-icon"
                  onClick={toggleLanguage}
                  title={language === 'pt' ? 'Switch to English' : 'Mudar para Português'}
                >
                  <Globe size={16} />
                  <span style={{ marginLeft: '4px', fontSize: '10px' }}>{language.toUpperCase()}</span>
                </button>
                <button 
                  className="btn-icon"
                  onClick={toggleTheme}
                  title={theme === 'light' ? 'Switch to Dark Mode' : 'Switch to Light Mode'}
                >
                  {theme === 'light' ? <Moon size={16} /> : <Sun size={16} />}
                </button>
              </div>
            </div>
          </nav>
        </div>
      </header>

      {/* Hero Section */}
      <section className="hero">
        <div className="container">
          <div className="hero-content">
            <div className="label">{currentData.sections.hero.label}</div>
            <h1 className="hero-title">{currentData.personalInfo.name}</h1>
            <div className="text-big">{currentData.personalInfo.title}</div>
            <div className="text-regular">{currentData.personalInfo.subtitle}</div>
            <div className="hero-status">
              <span className="label-small">{currentData.personalInfo.status}</span>
            </div>
            <div className="hero-actions">
              <button 
                className="btn-accent"
                onClick={() => scrollToSection('contato')}
              >
                {currentData.sections.hero.cta1}
              </button>
              <button 
                className="btn-primary"
                onClick={() => scrollToSection('sobre')}
              >
                {currentData.sections.hero.cta2}
              </button>
            </div>
          </div>
        </div>
      </section>

      {/* About Section */}
      <section id="sobre" className="section">
        <div className="container">
          <div className="section-header">
            <div className="label">{currentData.sections.about.label}</div>
            <h2 className="title-big">{currentData.sections.about.title}</h2>
          </div>
          <div className="about-content">
            <div className="about-text">
              <p className="text-body">{currentData.personalInfo.description}</p>
              <div className="about-details">
                <div className="detail-item">
                  <MapPin className="detail-icon" />
                  <span className="label-small">{currentData.personalInfo.location}</span>
                </div>
                <div className="detail-item">
                  <User className="detail-icon" />
                  <span className="label-small">
                    {language === 'pt' ? 'AUTODIDATA & DEDICADO' : 'SELF-TAUGHT & DEDICATED'}
                  </span>
                </div>
              </div>
            </div>
            <div className="education-goals">
              <div className="education-section">
                <div className="card">
                  <div className="label">{currentData.sections.about.formationTitle}</div>
                  {currentData.education?.map((edu, index) => (
                    <div key={index} className="education-item">
                      <div className="text-regular">{edu.degree}</div>
                      <div className="text-body">{edu.institution}</div>
                      <div className="label-small">{edu.period} • {edu.status}</div>
                    </div>
                  ))}
                </div>
              </div>
              <div className="goals-section">
                <div className="card">
                  <div className="label">{currentData.sections.about.goalsTitle}</div>
                  {currentData.goals?.map((goal, index) => (
                    <div key={index} className="goal-item">
                      <Target className="goal-icon" />
                      <span className="text-body">{goal}</span>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Skills Section */}
      <section id="habilidades" className="section">
        <div className="container">
          <div className="section-header">
            <div className="label">{currentData.sections.skills.label}</div>
            <h2 className="title-big">{currentData.sections.skills.title}</h2>
          </div>
          <div className="skills-grid">
            {currentData.skills?.map((skillGroup, index) => (
              <div key={index} className="card skill-card">
                <div className="skill-header">
                  <Code className="skill-icon" />
                  <div className="label">{skillGroup.category}</div>
                </div>
                <div className="skill-list">
                  {skillGroup.technologies?.map((tech, techIndex) => (
                    <span key={techIndex} className="skill-tag">
                      {tech}
                    </span>
                  ))}
                </div>
              </div>
            ))}
          </div>
          <div className="learning-section">
            <div className="card">
              <div className="label">{currentData.sections.skills.currentlyLearning}</div>
              <div className="learning-list">
                {currentData.currentLearning?.map((item, index) => (
                  <div key={index} className="learning-item">
                    <GraduationCap className="learning-icon" />
                    <span className="text-body">{item}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Contact Section */}
      <section id="contato" className="section">
        <div className="container">
          <div className="section-header">
            <div className="label">{currentData.sections.contact.label}</div>
            <h2 className="title-big">{currentData.sections.contact.title}</h2>
          </div>
          <div className="contact-content">
            <div className="contact-info">
              <p className="text-body">
                {currentData.sections.contact.description}
              </p>
              <div className="contact-links">
                <a href={`mailto:${currentData.contact.email}`} className="contact-link">
                  <Mail className="contact-icon" />
                  <span className="label">EMAIL</span>
                  <span className="contact-value">{currentData.contact.email}</span>
                </a>
                <a href={currentData.contact.linkedin} target="_blank" rel="noopener noreferrer" className="contact-link">
                  <Linkedin className="contact-icon" />
                  <span className="label">LINKEDIN</span>
                  <span className="contact-value">
                    {language === 'pt' ? 'Perfil Profissional' : 'Professional Profile'}
                  </span>
                </a>
                <a href={currentData.contact.github} target="_blank" rel="noopener noreferrer" className="contact-link">
                  <Github className="contact-icon" />
                  <span className="label">GITHUB</span>
                  <span className="contact-value">
                    {language === 'pt' ? 'Perfil Profissional' : 'Professional Profile'}
                  </span>
                </a>
              </div>
            </div>
            <div className="contact-action">
              <div className="card">
                <div className="label">{currentData.sections.contact.availableFor}</div>
                <div className="availability-list">
                  {currentData.sections.contact.availability?.map((item, index) => (
                    <div key={index} className="availability-item">
                      <span className="text-body">{item}</span>
                    </div>
                  ))}
                </div>
                <button 
                  className="btn-accent"
                  onClick={() => window.open(`mailto:${currentData.contact.email}?subject=${currentData.sections.contact.emailSubject}`, '_blank')}
                >
                  {currentData.sections.contact.sendEmail}
                </button>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="footer">
        <div className="container">
          <div className="footer-content">
            <div className="header-logo">@GomesDev1</div>
            <div className="footer-text">
              <span className="label-small">
                © 2024 • {language === 'pt' ? 'DESENVOLVIDO POR @GomesDev1' : 'DEVELOPED BY @GomesDev1'}
                {!isOnline && (
                  <span style={{ color: 'var(--color-warning)', marginLeft: '8px' }}>
                    • {language === 'pt' ? 'MODO' : 'MODE'}
                  </span>
                )}
              </span>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default Portfolio;