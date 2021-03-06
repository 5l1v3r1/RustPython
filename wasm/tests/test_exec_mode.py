def test_eval_mode(wdriver):
    assert wdriver.execute_script("return window.rp.pyEval('1+1')") == 2

def test_exec_mode(wdriver):
    assert wdriver.execute_script("return window.rp.pyExec('1+1')") is None

def test_exec_single_mode(wdriver):
    assert wdriver.execute_script("return window.rp.pyExecSingle('1+1')") == 2
    assert wdriver.execute_script(
        """
        var output = [];
        save_output = function(text) {{
           output.push(text)
        }};
        window.rp.pyExecSingle('1+1\\n2+2',{stdout: save_output});
        return output;
        """
    ) == ["2\n", "4\n"]
