# Portfolio Backend API Contracts

## Overview
Backend APIs para gerenciar dados do portfolio de Pedro Gomes, incluindo informações pessoais, habilidades, projetos, educação e configurações de usuário.

## Database Models

### 1. PersonalInfo
```javascript
{
  _id: ObjectId,
  name: String,
  title: {
    pt: String,
    en: String
  },
  subtitle: {
    pt: String, 
    en: String
  },
  description: {
    pt: String,
    en: String
  },
  location: String,
  status: {
    pt: String,
    en: String
  },
  contact: {
    email: String,
    linkedin: String,
    github: String
  },
  createdAt: Date,
  updatedAt: Date
}
```

### 2. Skills
```javascript
{
  _id: ObjectId,
  category: {
    pt: String,
    en: String
  },
  technologies: [String],
  order: Number,
  isActive: Boolean,
  createdAt: Date,
  updatedAt: Date
}
```

### 3. Education
```javascript
{
  _id: ObjectId,
  institution: String,
  degree: {
    pt: String,
    en: String
  },
  period: String,
  status: {
    pt: String,
    en: String
  },
  order: Number,
  isActive: Boolean,
  createdAt: Date,
  updatedAt: Date
}
```

### 4. Projects
```javascript
{
  _id: ObjectId,
  title: {
    pt: String,
    en: String
  },
  description: {
    pt: String,
    en: String
  },
  technologies: [String],
  githubUrl: String,
  liveUrl: String,
  imageUrl: String,
  status: String, // 'active', 'development', 'placeholder'
  featured: Boolean,
  order: Number,
  createdAt: Date,
  updatedAt: Date
}
```

### 5. Goals
```javascript
{
  _id: ObjectId,
  goal: {
    pt: String,
    en: String
  },
  order: Number,
  isActive: Boolean,
  createdAt: Date,
  updatedAt: Date
}
```

### 6. CurrentLearning
```javascript
{
  _id: ObjectId,
  item: {
    pt: String,
    en: String
  },
  order: Number,
  isActive: Boolean,
  createdAt: Date,
  updatedAt: Date
}
```

## API Endpoints

### Personal Info
- `GET /api/personal-info` - Obter informações pessoais
- `PUT /api/personal-info` - Atualizar informações pessoais

### Skills
- `GET /api/skills` - Listar habilidades ativas ordenadas
- `POST /api/skills` - Criar nova habilidade
- `PUT /api/skills/:id` - Atualizar habilidade
- `DELETE /api/skills/:id` - Deletar habilidade

### Education
- `GET /api/education` - Listar educação ativa ordenada
- `POST /api/education` - Criar nova educação
- `PUT /api/education/:id` - Atualizar educação
- `DELETE /api/education/:id` - Deletar educação

### Projects
- `GET /api/projects` - Listar projetos ativos ordenados
- `GET /api/projects/featured` - Listar projetos em destaque
- `POST /api/projects` - Criar novo projeto
- `PUT /api/projects/:id` - Atualizar projeto
- `DELETE /api/projects/:id` - Deletar projeto

### Goals
- `GET /api/goals` - Listar objetivos ativos ordenados
- `POST /api/goals` - Criar novo objetivo
- `PUT /api/goals/:id` - Atualizar objetivo
- `DELETE /api/goals/:id` - Deletar objetivo

### Current Learning
- `GET /api/current-learning` - Listar itens de aprendizado atuais
- `POST /api/current-learning` - Criar novo item
- `PUT /api/current-learning/:id` - Atualizar item
- `DELETE /api/current-learning/:id` - Deletar item

### Portfolio Data (Aggregate)
- `GET /api/portfolio` - Obter todos os dados do portfolio em uma chamada

## Frontend Integration Plan

### Current Mock Data Location
- `/app/frontend/src/mock/data.js` - Dados mockados multilíngues

### Integration Steps
1. Criar hook customizado `usePortfolio()` para gerenciar dados
2. Substituir imports do mock data por chamadas API
3. Implementar loading states e error handling
4. Manter estrutura de dados compatível com componentes existentes

### API Client Structure
```javascript
// /app/frontend/src/services/api.js
const API_BASE = process.env.REACT_APP_BACKEND_URL + '/api';

export const portfolioAPI = {
  getPortfolioData: () => fetch(`${API_BASE}/portfolio`),
  getPersonalInfo: () => fetch(`${API_BASE}/personal-info`),
  getSkills: () => fetch(`${API_BASE}/skills`),
  getEducation: () => fetch(`${API_BASE}/education`),
  getProjects: () => fetch(`${API_BASE}/projects`),
  getGoals: () => fetch(`${API_BASE}/goals`),
  getCurrentLearning: () => fetch(`${API_BASE}/current-learning`)
};
```

### Data Transformation
- Backend retorna dados no formato correto para frontend
- Frontend mantém estrutura `data[language]` para compatibilidade
- Hook `usePortfolio()` gerencia language switching

## Error Handling
- Padrão de resposta para erros: `{ success: false, error: "message", code: "ERROR_CODE" }`
- Fallback para dados mockados em caso de erro de API
- Toast notifications para operações CRUD

## Seed Data
Backend será inicializado com dados baseados no mock atual, convertidos para formato multilíngue estruturado.

## Testing Strategy
- Testar todas as rotas CRUD com curl
- Verificar integração frontend-backend
- Validar switching de idiomas com dados reais
- Confirmar fallback behavior