import axios from 'axios';

export const validateReport = async (report) => {
  // Your AI validation logic
  const response = await axios.post('/api/validate', { report });
  return response.data;
};