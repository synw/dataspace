const libName = "dataspace";
const libTitle = "Dataspace";
const repoUrl = "https://github.com/synw/dataspace";

const links: Array<{ href: string; name: string }> = [
  // { href: "/python", name: "Python api" },
];

// python runtime
const pipPackages = [];
const pyodidePackages = [];
const examplesExtension = "py";

async function loadHljsTheme(isDark: boolean) {
  if (isDark) {
    await import("../node_modules/highlight.js/styles/base16/material-darker.css")
  } else {
    await import("../node_modules/highlight.js/styles/stackoverflow-light.css")
  }
}

/** Import the languages you need for highlighting */
import hljs from 'highlight.js/lib/core';
import python from 'highlight.js/lib/languages/python';
//import bash from 'highlight.js/lib/languages/bash';
//import typescript from 'highlight.js/lib/languages/typescript';
//import xml from 'highlight.js/lib/languages/xml';
//import json from 'highlight.js/lib/languages/json';
hljs.registerLanguage('python', python);
//hljs.registerLanguage('typescript', typescript);
//hljs.registerLanguage('bash', bash);
//hljs.registerLanguage('html', xml);
//hljs.registerLanguage('json', json);

// some Python code to run after install
const initCode: string | undefined = undefined;

export {
  libName,
  libTitle,
  repoUrl,
  pipPackages,
  examplesExtension,
  pyodidePackages,
  links,
  hljs,
  initCode,
  loadHljsTheme
}