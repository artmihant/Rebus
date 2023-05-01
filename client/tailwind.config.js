/** @type {import('tailwindcss').Config} */
module.exports = {
  purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    screens: {
        sm: '480px',
        md: '860px',
        lg: '1220px',
        xl: '1440px',
    },
    extend: {},
  },
  plugins: [],
}

