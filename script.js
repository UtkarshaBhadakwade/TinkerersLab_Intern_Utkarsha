/* ===============================
   SIDEBAR MENU
=================================*/
function toggleMenu() {

    const sidebar = document.getElementById("sidebar");

    if (sidebar.style.left === "0px") {
        sidebar.style.left = "-250px";
    } else {
        sidebar.style.left = "0px";
    }
}


/* ===============================
   SCROLL FUNCTION (HOME PAGE)
=================================*/
function scrollDown() {

    const section = document.getElementById("overview");

    if (section) {
        section.scrollIntoView({ behavior: "smooth" });
    }
}


/* ===============================
   OPEN WEEK
=================================*/
function openWeek(weekId) {

    // Hide week grid
    const weeksGrid = document.getElementById("weeksGrid");
    if (weeksGrid) {
        weeksGrid.style.display = "none";
    }

    // Hide all weeks
    document.querySelectorAll(".week-full")
        .forEach(week => week.style.display = "none");

    // Show selected week
    const selectedWeek = document.getElementById(weekId);
    if (selectedWeek) {
        selectedWeek.style.display = "block";
    }
}


/* ===============================
   CLOSE WEEK
=================================*/
function closeWeek() {

    // Show week grid again (GRID, not FLEX)
    const weeksGrid = document.getElementById("weeksGrid");
    if (weeksGrid) {
        weeksGrid.style.display = "grid";
    }

    // Hide all week pages
    document.querySelectorAll(".week-full")
        .forEach(week => week.style.display = "none");
}


/* ===============================
   OPEN DAY
=================================*/
function openDay(dayId) {

    // Hide day grid
    const dayGrid = document.getElementById("dayGrid");
    if (dayGrid) {
        dayGrid.style.display = "none";
    }

    // Hide all day pages
    document.querySelectorAll(".day-full")
        .forEach(day => day.style.display = "none");

    // Show selected day
    const selectedDay = document.getElementById(dayId);
    if (selectedDay) {
        selectedDay.style.display = "block";
    }
}


/* ===============================
   CLOSE DAY
=================================*/
function closeDay() {

    // Show day grid again (GRID, not FLEX)
    const dayGrid = document.getElementById("dayGrid");
    if (dayGrid) {
        dayGrid.style.display = "grid";
    }

    // Hide all day pages
    document.querySelectorAll(".day-full")
        .forEach(day => day.style.display = "none");
}