// @ts-check
const eslint = require("@eslint/js");
const tseslint = require("typescript-eslint");
const angular = require("angular-eslint");

module.exports = tseslint.config(
  {
    files: ["**/*.ts"],
    extends: [
      eslint.configs.recommended,
      ...tseslint.configs.recommended,
      ...tseslint.configs.stylistic,
      ...angular.configs.tsRecommended,
    ],
    processor: angular.processInlineTemplates,
    rules: {
     // TypeScript / Google Style Regeln
      "@typescript-eslint/explicit-function-return-type": "error",
      "@typescript-eslint/no-explicit-any": "error",
      "@typescript-eslint/no-unused-vars": [
        "error",
        { argsIgnorePattern: "^_", varsIgnorePattern: "^_" }
      ],
      "@typescript-eslint/consistent-type-imports": "error",
      "quotes": ["error", "double"],
      "semi": ["error", "always"],
      "indent": ["error", 2, { SwitchCase: 1 }],
      "brace-style": ["error", "1tbs", { allowSingleLine: true }],
      "eqeqeq": ["error", "always"],
      "prefer-const": "error",
      "no-console": ["warn", { allow: ["warn", "error"] }],

      // Angular spezifische Regeln
      "@angular-eslint/directive-selector": ["error", { type: "attribute", prefix: "app", style: "camelCase" }],
      "@angular-eslint/component-selector": ["error", { type: "element", prefix: "app", style: "kebab-case" }],

      // Komplexitätsregeln nach Google-ähnlichem Standard
      "max-depth": ["error", 3],
      "complexity": ["error", { "max": 10 }],
      "max-lines-per-function": ["error", { max: 50, skipComments: true, skipBlankLines: true }],
      "max-params": ["error", 4],
      "max-nested-callbacks": ["error", 3]
    },
  },
  {
    files: ["**/*.html"],
    extends: [
      ...angular.configs.templateRecommended,
      ...angular.configs.templateAccessibility,
    ],
    rules: {
        "max-len": ["error", { code: 140 }]
    },
  }
);
