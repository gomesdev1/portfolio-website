import React, { useState } from 'react';
import { mockData } from '../mock/data';
import { Mail, Github, Linkedin, MapPin, Calendar, Code, GraduationCap, Target, User, Briefcase } from 'lucide-react';

const Portfolio = () => {
  const [activeSection, setActiveSection] = useState('sobre');

  const scrollToSection = (sectionId) => {
    const element = document.getElementById(sectionId);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
      setActiveSection(sectionId);
    }
  };

  return (
    <div className="portfolio">
      {/* Grid Background */}
      <div className="grid-background"></div>
      
      {/* Header */}
      <header className="header">
        <div className="container">
          <nav className="nav">
            <div className="header-logo">DEV.PORTFOLIO</div>
            <div className="nav-menu">
              <a href="#sobre" className="nav-link" onClick={(e) => { e.preventDefault(); scrollToSection('sobre'); }}>
                SOBRE
              </a>
              <a href="#habilidades" className="nav-link" onClick={(e) => { e.preventDefault(); scrollToSection('habilidades'); }}>
                HABILIDADES
              </a>
              <a href="#projetos" className="nav-link" onClick={(e) => { e.preventDefault(); scrollToSection('projetos'); }}>
                PROJETOS
              </a>
              <a href="#contato" className="nav-link" onClick={(e) => { e.preventDefault(); scrollToSection('contato'); }}>
                CONTATO
              </a>
            </div>
          </nav>
        </div>
      </header>

      {/* Hero Section */}
      <section className="hero">
        <div className="container">
          <div className="hero-content">
            <div className="label">DESENVOLVEDOR EM FORMAÇÃO</div>
            <h1 className="hero-title">{mockData.personalInfo.name}</h1>
            <div className="text-big">{mockData.personalInfo.title}</div>
            <div className="text-regular">{mockData.personalInfo.subtitle}</div>
            <div className="hero-status">
              <span className="label-small">{mockData.personalInfo.status}</span>
            </div>
            <div className="hero-actions">
              <button 
                className="btn-accent"
                onClick={() => scrollToSection('contato')}
              >
                ENTRAR EM CONTATO
              </button>
              <button 
                className="btn-primary"
                onClick={() => scrollToSection('sobre')}
              >
                CONHECER MAIS
              </button>
            </div>
          </div>
        </div>
      </section>

      {/* About Section */}
      <section id="sobre" className="section">
        <div className="container">
          <div className="section-header">
            <div className="label">QUEM SOU EU</div>
            <h2 className="title-big">SOBRE</h2>
          </div>
          <div className="about-content">
            <div className="about-text">
              <p className="text-body">{mockData.personalInfo.description}</p>
              <div className="about-details">
                <div className="detail-item">
                  <MapPin className="detail-icon" />
                  <span className="label-small">{mockData.personalInfo.location}</span>
                </div>
                <div className="detail-item">
                  <User className="detail-icon" />
                  <span className="label-small">AUTODIDATA & DEDICADO</span>
                </div>
              </div>
            </div>
            <div className="education-goals">
              <div className="education-section">
                <div className="card">
                  <div className="label">FORMAÇÃO</div>
                  {mockData.education.map((edu, index) => (
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
                  <div className="label">OBJETIVOS</div>
                  {mockData.goals.map((goal, index) => (
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
            <div className="label">CONHECIMENTOS</div>
            <h2 className="title-big">HABILIDADES</h2>
          </div>
          <div className="skills-grid">
            {mockData.skills.map((skillGroup, index) => (
              <div key={index} className="card skill-card">
                <div className="skill-header">
                  <Code className="skill-icon" />
                  <div className="label">{skillGroup.category}</div>
                </div>
                <div className="skill-list">
                  {skillGroup.technologies.map((tech, techIndex) => (
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
              <div className="label">ATUALMENTE ESTUDANDO</div>
              <div className="learning-list">
                {mockData.currentLearning.map((item, index) => (
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

      {/* Projects Section */}
      <section id="projetos" className="section">
        <div className="container">
          <div className="section-header">
            <div className="label">PORTFÓLIO</div>
            <h2 className="title-big">PROJETOS</h2>
          </div>
          <div className="projects-content">
            <div className="card projects-placeholder">
              <Briefcase className="placeholder-icon" />
              <div className="text-regular">PROJETOS EM DESENVOLVIMENTO</div>
              <p className="text-body">
                Esta seção será preenchida conforme novos projetos forem desenvolvidos durante meus estudos e práticas.
              </p>
              <div className="label-small">AGUARDE ATUALIZAÇÕES</div>
            </div>
          </div>
        </div>
      </section>

      {/* Contact Section */}
      <section id="contato" className="section">
        <div className="container">
          <div className="section-header">
            <div className="label">VAMOS CONVERSAR</div>
            <h2 className="title-big">CONTATO</h2>
          </div>
          <div className="contact-content">
            <div className="contact-info">
              <p className="text-body">
                Estou em busca da minha primeira oportunidade de estágio para aplicar meus conhecimentos e continuar aprendendo.
              </p>
              <div className="contact-links">
                <a href={`mailto:${mockData.contact.email}`} className="contact-link">
                  <Mail className="contact-icon" />
                  <span className="label">EMAIL</span>
                  <span className="contact-value">{mockData.contact.email}</span>
                </a>
                <a href={mockData.contact.linkedin} target="_blank" rel="noopener noreferrer" className="contact-link">
                  <Linkedin className="contact-icon" />
                  <span className="label">LINKEDIN</span>
                  <span className="contact-value">Perfil Profissional</span>
                </a>
                <a href={mockData.contact.github} target="_blank" rel="noopener noreferrer" className="contact-link">
                  <Github className="contact-icon" />
                  <span className="label">GITHUB</span>
                  <span className="contact-value">Repositórios</span>
                </a>
              </div>
            </div>
            <div className="contact-action">
              <div className="card">
                <div className="label">DISPONÍVEL PARA</div>
                <div className="availability-list">
                  <div className="availability-item">
                    <span className="text-body">• Estágio em Desenvolvimento</span>
                  </div>
                  <div className="availability-item">
                    <span className="text-body">• Projetos de Aprendizado</span>
                  </div>
                  <div className="availability-item">
                    <span className="text-body">• Mentorias</span>
                  </div>
                  <div className="availability-item">
                    <span className="text-body">• Networking</span>
                  </div>
                </div>
                <button 
                  className="btn-accent"
                  onClick={() => window.open(`mailto:${mockData.contact.email}?subject=Oportunidade de Estágio`, '_blank')}
                >
                  ENVIAR EMAIL
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
            <div className="header-logo">DEV.PORTFOLIO</div>
            <div className="footer-text">
              <span className="label-small">© 2024 • DESENVOLVIDO COM DEDICAÇÃO</span>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default Portfolio;