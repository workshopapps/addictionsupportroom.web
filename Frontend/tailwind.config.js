/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        blue: "#0E8ACB",
        grey: "#3E3E3E"
      },
      screens: {
        mobile: "360px",
        tablet: "480px",
        laptop: "780px",
        desktop: "1020px",
        xl: "1400px",
      },
    },
  },
  plugins: []
}
