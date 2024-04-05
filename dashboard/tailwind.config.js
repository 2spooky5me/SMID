/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      backgroundImage: {
        'header-carnet': "url('/src/assets/img/bg-header.svg')",
      },
      colors: {
        orangecpv: {
          100: "#ffe2cc",
          200: "#ffc599",
          300: "#ffa766",
          400: "#ff8a33",
          500: "#ff6d00",
          600: "#cc5700",
          700: "#994100",
          800: "#662c00",
          900: "#331600"
        },
        cyancpv: {
          100: "#d7f2ee",
          200: "#aee4de",
          300: "#86d7cd",
          400: "#5dc9bd",
          500: "#35bcac",
          600: "#2a968a",
          700: "#207167",
          800: "#154b45",
          900: "#0b2622"
        },

        

      },
    },
  },
  plugins: [],
}