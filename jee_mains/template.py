TEMPLATE = """
<!DOCTYPE html>
<html lang="en-US">

<head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>DevParapalli's JEE Mains App</title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <style>{styles}</style>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/materialize-css@1.0.0/dist/css/materialize.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.1/css/bulma.min.css">
</head>

<body class="is-dark">
    <section>
        <div class="container is-fluid">
            <h1 class="title">DevParapalli/JEE-Mains</h1>
            <a onclick="window.print()" class="button is-primary is-light no-print">Print</a>
            <hr />
            <h2 class="subtitle">Section A</h2>
            <table class="table" aria-describedby="Table containing">
                <thead>
                    <tr>
                        <th id="heading">Information</th>
                        <th id="blank"></th>
                    </tr>
                </thead>
                <tr>
                    <td><strong>Name</strong></td>
                    <td>{name}</td>
                </tr>
                <tr>
                    <td><strong>Application Number</strong></td>
                    <td>{admission_number}</td>
                </tr>
                <tr>
                    <td><strong>Roll Number</strong></td>
                    <td>{roll_number}</td>
                </tr>
                <tr>
                    <td><strong>Test Date</strong></td>
                    <td>{test_date}</td>
                </tr>
                <tr>
                    <td><strong>Test Time</strong></td>
                    <td>{test_time}</td>
                </tr>
                <tr>
                    <td><strong>Subject</strong></td>
                    <td>{subject}</td>
                </tr>
                <tr>
                    <td><strong>Marks Obtained</strong></td>
                    <td>{marks_obtained}</td>
                </tr>
                <tr>
                    <td><strong>Inferred Shift Code</strong></td>
                    <td>{shift_code}</td>
                </tr>
            </table>
            <hr style="page-break-before: always;" />
            <h2 class="subtitle">Section B</h2>
            <table class="table" aria-describedby="table representing the marks tally">
                <thead>
                    <tr>
                        <th id="q_left">Subject</th>
                        <th id="q_left">Questions Correct</th>
                        <th id="q_left">Questions Incorrect</th>
                        <th id="q_left">Questions Left</th>
                    </tr>
                </thead>

                <tbody>
                    <tr>
                        <td><strong>Physics - MCQ</strong></td>
                        <td>{physics_scq_correct}</td>
                        <td>{physics_scq_incorrect}</td>
                        <td>{physics_scq_left}</td>
                    </tr>
                    <tr>
                        <td><strong>Physics - Integer</strong></td>
                        <td>{physics_int_correct}</td>
                        <td>{physics_int_incorrect}</td>
                        <td>{physics_int_left}</td>
                    </tr>
                    <tr>
                        <td><strong>Chemistry - MCQ</strong></td>
                        <td>{chemistry_scq_correct}</td>
                        <td>{chemistry_scq_incorrect}</td>
                        <td>{chemistry_scq_left}</td>
                    </tr>
                    <tr>
                        <td><strong>Chemistry - Integer</strong></td>
                        <td>{chemistry_int_correct}</td>
                        <td>{chemistry_int_incorrect}</td>
                        <td>{chemistry_int_left}</td>
                    </tr>
                    <tr>
                        <td><strong>Maths - MCQ</strong></td>
                        <td>{maths_scq_correct}</td>
                        <td>{maths_scq_incorrect}</td>
                        <td>{maths_scq_left}</td>
                    </tr>
                    <tr>
                        <td><strong>Maths - Integer</strong></td>
                        <td>{maths_int_correct}</td>
                        <td>{maths_int_incorrect}</td>
                        <td>{maths_int_left}</td>
                    </tr>
                    <tr>
                        <td><strong>Total</strong></td>
                        <td><strong>{total_correct}</strong></td>
                        <td><strong>{total_incorrect}</strong></td>
                        <td><strong>{total_left}</strong></td>
                    </tr>
                </tbody>
                
            </table>
            <hr style="page-break-before: always;" />
            <h2 class="subtitle">Section C</h2>
            Raw JSON:
            <pre><code>{raw_json}</code></pre>
        </div>
    </section>
    <section class="footer">
        <span class="footer-copyright">Made with ❤️ by DevParapalli. © DevParapalli 2021</>
    </section>
</body>

</html>
"""

# NOTE: Styles is "@media print{ .no-print{visibility:hidden}}""
if __name__ == "__main__":
    import string
    print(" = \"\"\n".join([i[1] for i in string.Formatter().parse(TEMPLATE) if i[1] is not None]))
