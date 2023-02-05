const colors = require('tailwindcss/colors');

module.exports = {
  content: [
    './index.html',
    './src/**/*.{js,jsx,ts,tsx,vue}',
    './node_modules/@snowind/**/*.{vue,js,ts}',
    './node_modules/vuepython/**/*.{vue,js,ts}',
  ],
  darkMode: 'class',
  plugins: [
    require('@tailwindcss/forms'),
    require('@snowind/plugin'),
    require('tailwindcss-semantic-colors')
  ],
  theme: {
    extend: {
      semanticColors: {
        primary: {
          light: {
            bg: colors.cyan[800],
            txt: colors.white
          },
          dark: {
            bg: colors.neutral[900],
            txt: colors.neutral[100]
          }
        },
        secondary: {
          light: {
            bg: colors.cyan[500],
            txt: colors.white
          },
          dark: {
            bg: colors.neutral[800],
            txt: colors.neutral[100]
          }
        },
        secondary2: {
          light: {
            bg: colors.cyan[600],
            txt: colors.white
          },
          dark: {
            bg: colors.neutral[800],
            txt: colors.neutral[100]
          }
        },
      }
    }
  }
}