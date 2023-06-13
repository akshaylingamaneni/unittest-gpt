
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
unittest-gpt
</h1>
<h3 align="center">📍 Test smarter, not harder with unittest-gpt: GPT-powered auto unit tests generator!</h3>
<h3 align="center">⚙️ Developed with the software and tools below:</h3>

> <h3 align="center">⚙️ Powered by OpenAI's GPT language model APIs and the software below:</h3>
>  <p align="center">
>   🦜️🔗
>   <img src="https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white" alt="OpenAI" />
>   <img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="Python" />
>   <img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=for-the-badge&logo=Pytest&logoColor=white" alt="pytest" />
> </p>

<p align="center">

</p>
</div>

---

## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [💫 Features](#-features)
- [📂 Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🚀 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

unittest-gpt is a powerful, user-friendly tool that automatically generates unit test files for your python repositories using OpenAI's language model APIs. By simply providing the file or a directory, unittest-gpt will automatically generate unit test for your python source code.

---


## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - 📌  OPENAI - API KEY
> - 📌  Python 3.11

---
#### 🔐 OpenAI API Setup

To use README-AI, you will need an API key for OpenAI. Follow the steps below to create an API key:

<details closed>
<summary>User Guide - OpenAI API</summary>

1. Go to the [OpenAI website](https://platform.openai.com/).
2. Click the "Sign up for free" button.
3. Fill out the registration form with your information and agree to the terms of service.
4. Once logged in, click on the "API" tab.
5. Follow the instructions to create a new API key.
6. Copy the API key and keep it in a secure place.

</details>

---
### 🖥 Installation

1. Clone the unittest-gpt repository:
```sh
git clone ../unittest-gpt
```

2. Change to the project directory:
```sh
cd unittest-gpt
```
3. Setup up a venv (the least resistance way to get started quickly) 
   1. if you don't have virtualenv install run the first command
```sh
pip install virtualenv 

virtualenv venv

source venv/bin/activate
```
3. Install the dependencies:
```sh
pip install -r requirements.txt
```

### 🤖 Using unittest-gpt as cli
```sh
python unit_test_agent.py -f <file_name>
python unit_test_agent.py -dir <dir_name>
#example
python unit_test_agent.py -f test.py
python unit_test_agent.py -dir src


```

### 🤖 Using unittest-gpt in your project
```sh
unit_test_agent = UnitTestAgent()
# Call the method with the file parameter
unit_test_agent.generate_testcases(file="<file_name>")
# Call the method with the directory parameter
unit_test_agent.generate_testcases(path="<directory>")


```

### 🧪 Running Tests
Run below command in the root directory
```sh
pytest
```

---


## 🤝 Contributing

Contributions are always welcome! Please follow these steps:
1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).
```sh
git checkout -b new-feature-branch
```
4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub using the following command
```sh
git push origin new-feature-branch
```
7. Create a pull request to the original repository.
Open a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 📄 License

This project is licensed under the `MIT License` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 👏 Acknowledgments
 - [hwchase17/langchain](https://github.com/hwchase17/langchain.git) wouldn't have built without langchain.
- [gkamradt/langchain-tutorials](https://github.com/gkamradt/langchain-tutorials.git) his videos are inspiring and open your imagination to build cool things.
- [eli64s/README-AI](https://github.com/eli64s/README-AI.git) thanks for helping me set up a quick readme.md file. Will use it for all projects going forward.

---
