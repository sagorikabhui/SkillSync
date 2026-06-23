function showNotification(message) {

    const notification =
        document.getElementById("notification");

    if (!notification) return;

    notification.textContent = message;

    notification.classList.add("show");

    setTimeout(function () {

        notification.classList.remove("show");

    }, 3000);

}

const searchInput =
    document.getElementById("searchInput");

if (searchInput) {

    searchInput.addEventListener("keyup", function () {

        const searchValue =
            searchInput.value
                .toLowerCase()
                .trim();

        console.log(
            "[" + searchValue + "]"
        );
        const studentCards =
            document.querySelectorAll(".student-card");

        let visibleCount = 0;
        studentCards.forEach(function (card) {

            const name =
                card.dataset.name.toLowerCase();

            const skills =
                card.dataset.skills
                    .toLowerCase()
                    .split(" ");

            console.log("Name:", name);
            console.log("Skills:", skills);
            console.log("----------------");

            const nameMatch =
                name.includes(searchValue);

            const skillMatch =
                skills.includes(searchValue);

            if (searchValue === "javascript") {
                console.log(skills);
            }

            console.log(
                searchValue,
                "=>",
                skillMatch
            );

            if (
                searchValue === "" ||
                nameMatch ||
                skillMatch
            ) {

                card.style.display = "block";
                visibleCount++;

            } else {

                card.style.display = "none";

            }

        });
        const studentCount =
            document.getElementById("studentCount");

        if (studentCount) {

            studentCount.textContent =
                visibleCount +
                (visibleCount === 1
                    ? " Student Found"
                    : " Students Found");

        }

    });

}


const joinButtons =
    document.querySelectorAll(".join-btn");

joinButtons.forEach(function (button) {

    button.addEventListener("click", function () {

        if (
            button.textContent === "Join Group"
        ) {

            button.textContent = "Joined ✓";
            showNotification(
                "Group Joined Successfully ✓"
            );

            button.classList.add("joined");

        } else {

            button.textContent = "Join Group";

            button.classList.remove("joined");

        }

    });

});

const connectButtons =
    document.querySelectorAll(".connect-btn");

connectButtons.forEach(function (button) {

    button.addEventListener("click", function () {

        if (
            button.textContent === "Connect"
        ) {

            button.textContent =
                "Request Sent ✓";

            showNotification(
                "Connection Request Sent ✓"
            );

            button.classList.add("connected");

        } else {

            button.textContent = "Connect";

            button.classList.remove("connected");

        }

    });

});

const projectButtons =
    document.querySelectorAll(".project-btn");

projectButtons.forEach(function (button) {

    button.addEventListener("click", function () {

        if (
            button.textContent === "Join Project"
        ) {

            button.textContent = "Applied ✓";
            showNotification(
                "Project Application Submitted ✓"
            );

            button.classList.add("applied");

        } else {

            button.textContent = "Join Project";

            button.classList.remove("applied");

        }

    });

});

const darkModeBtn =
    document.getElementById("darkModeBtn");

if (localStorage.getItem("theme") === "dark") {

    document.body.classList.add("dark-mode");

    if (darkModeBtn) {

        darkModeBtn.textContent =
            "☀ Light Mode";

    }

}

if (darkModeBtn) {

    darkModeBtn.addEventListener("click", function () {

        document.body.classList.toggle("dark-mode");

        if (
            document.body.classList.contains("dark-mode")
        ) {

            localStorage.setItem(
                "theme",
                "dark"
            );

            darkModeBtn.textContent =
                "☀ Light Mode";

        } else {

            localStorage.setItem(
                "theme",
                "light"
            );

            darkModeBtn.textContent =
                "🌙 Dark Mode";

        }

    });

}


// COUNTERS ANIMATE ON SCROLL

const counters =
    document.querySelectorAll(".counter");

let counterStarted = false;

function startCounters() {

    if (counterStarted) return;

    counterStarted = true;

    counters.forEach(function (counter) {

        const target =
            Number(counter.dataset.target);

        let current = 0;

        const updateCounter = function () {

            const increment =
                target / 50;

            if (current < target) {

                current += increment;

                counter.textContent =
                    Math.floor(current);

                setTimeout(
                    updateCounter,
                    20
                );

            } else {

                counter.textContent =
                    target + "+";

            }

        };

        updateCounter();

    });

}

window.addEventListener("scroll", function () {

    const statsSection =
        document.querySelector(".stats");

    if (!statsSection) return;

    const sectionTop =
        statsSection.getBoundingClientRect().top;

    if (sectionTop < window.innerHeight - 100) {

        startCounters();

    }

});

// PROJECT FILTER

const filterButtons =
    document.querySelectorAll(".filter-btn");

filterButtons.forEach(function (button) {

    button.addEventListener("click", function () {
        filterButtons.forEach(function (btn) {

            btn.classList.remove("active");

        });

        button.classList.add("active");

        const filter =
            button.dataset.filter;

        const projects =
            document.querySelectorAll(".project-card");

        projects.forEach(function (project) {

            if (
                filter === "all" ||
                project.dataset.category === filter
            ) {

                project.style.display = "block";

            } else {

                project.style.display = "none";

            }

        });

    });

});

// ACTIVE NAVBAR LINK

const currentPage =
    window.location.pathname
        .split("/")
        .pop();

const navLinks =
    document.querySelectorAll("nav a");

navLinks.forEach(function (link) {

    const linkPage =
        link.getAttribute("href");

    if (linkPage === currentPage) {

        link.classList.add("active-link");

    }

});

// SCROLL TO TOP BUTTON

const topBtn =
    document.getElementById("topBtn");

if (topBtn) {

    window.addEventListener("scroll", function () {

        if (window.scrollY > 300) {

            topBtn.style.display = "block";

        } else {

            topBtn.style.display = "none";

        }

    });

    topBtn.addEventListener("click", function () {

        window.scrollTo({

            top: 0,

            behavior: "smooth"

        });

    });

}

// REVEAL ANIMATION

const reveals =
    document.querySelectorAll(".reveal");

function revealElements() {

    reveals.forEach(function (element) {

        const windowHeight =
            window.innerHeight;

        const elementTop =
            element.getBoundingClientRect().top;

        if (elementTop < windowHeight - 100) {

            element.classList.add("active");

        }

    });

}

window.addEventListener(
    "scroll",
    revealElements
);

revealElements();


const typingText =
    document.getElementById("typingText");

if (typingText) {

    const text =
        "Find Skills.\nBuild Projects.\nGrow Together.";

    let index = 0;

    function typeWriter() {

        if (index < text.length) {

            if (text.charAt(index) === "\n") {

                typingText.innerHTML += "<br>";

            } else {

                typingText.innerHTML +=
                    text.charAt(index);

            }

            index++;

            setTimeout(typeWriter, 20);

        } else {

            typingText.innerHTML =
                typingText.innerHTML.replace(
                    "Skills",
                    '<span class="highlight">Skills</span>'
                );

        }

    }

    typeWriter();
}

const faqQuestions =
    document.querySelectorAll(".faq-question");

faqQuestions.forEach(function (question) {

    question.addEventListener("click", function () {

        const faqItem =
            question.parentElement;

        faqItem.classList.toggle("active");

    });

});

window.addEventListener("scroll", function () {

    const scrollTop =
        document.documentElement.scrollTop;

    const scrollHeight =
        document.documentElement.scrollHeight -
        document.documentElement.clientHeight;

    const scrollPercent =
        (scrollTop / scrollHeight) * 100;

    const progressBar =
        document.getElementById("progressBar");

    if (progressBar) {

        progressBar.style.width =
            scrollPercent + "%";
    }

});

const createProjectBtn =
    document.getElementById("createProjectBtn");

if (createProjectBtn) {

    createProjectBtn.addEventListener(
        "click",
        function () {

            const title =
                document.getElementById("projectTitle").value;

            const skills =
                document.getElementById("projectSkills").value;

            const members =
                document.getElementById("projectMembers").value;

            if (
                title === "" ||
                skills === "" ||
                members === ""
            ) {

                alert("Please fill all fields");

                return;
            }

            const projectCard =
                document.createElement("div");

            projectCard.classList.add("project-card");

            const skillArray = skills.split(",");

            let skillBadges = "";

            skillArray.forEach(skill => {

                skillBadges += `
        <span class="badge">
            ${skill.trim()}
        </span>
    `;
            });

            projectCard.innerHTML = `
            <h3>🚀 ${title}</h3>
            
            <p><strong>Skills Required:</strong></p>
            
            <div class="project-tags">
            
            ${skillBadges}
            
            </div>

            <p class="team-needed">
         
            👥 Need ${members} Members
            
            </p>
            
            <button class="project-btn">
            
            Join Project
            
            </button>
            
            `;
            document
                .querySelector(".projects-container")
                .appendChild(projectCard);

            document.getElementById("projectTitle").value = "";
            document.getElementById("projectSkills").value = "";
            document.getElementById("projectMembers").value = "";

            alert("Project Created Successfully!");
        }
    );
}


const menuBtn =
    document.getElementById("menuBtn");

const sidebar =
    document.getElementById("sidebar");

const overlay =
    document.getElementById("overlay");

let sidebarOpen = false;

menuBtn.addEventListener(
    "click",
    function () {

        if (sidebarOpen) {

            sidebar.style.left = "-250px";
            overlay.style.display = "none";

            sidebarOpen = false;

        } else {

            sidebar.style.left = "0";
            overlay.style.display = "block";

            sidebarOpen = true;

        }

    }
);

overlay.addEventListener(
    "click",
    function () {

        sidebar.style.left = "-250px";
        overlay.style.display = "none";

        sidebarOpen = false;

    }
);

const showGroupForm =
    document.getElementById("showGroupForm");

const groupForm =
    document.querySelector(".group-form");

if (showGroupForm && groupForm) {

    showGroupForm.addEventListener(
        "click",
        function () {

            if (
                groupForm.style.display === "block"
            ) {

                groupForm.style.display = "none";

                showGroupForm.textContent =
                    "Create Group";

            } else {

                groupForm.style.display = "block";

                showGroupForm.textContent =
                    "Close Form";

            }

        }
    );

}


const showProjectForm =
    document.getElementById("showProjectForm");

const projectForm =
    document.getElementById("projectForm");

if (showProjectForm && projectForm) {

    showProjectForm.addEventListener(
        "click",
        function () {

            if (
                projectForm.style.display === "block"
            ) {

                projectForm.style.display = "none";

                showProjectForm.textContent =
                    "Create Project";

            } else {

                projectForm.style.display = "block";

                showProjectForm.textContent =
                    "Close Form";

            }

        }
    );

}