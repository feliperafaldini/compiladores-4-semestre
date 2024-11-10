from parser import Parser


class CodeGenerator:
    def __init__(self):
        self.code = []
        self.temp_count = 0
        self.label_count = 0

    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    def new_label(self):
        self.label_count += 1
        return f"L{self.label_count}"

    def generate_code(self, node):

        if isinstance(node, list):
            for n in node:
                self.generate_code(n)
            return

        if isinstance(node, tuple):
            node_type = node[0]

            if node_type == "assign":
                target = node[1]
                expr = self.generate_code(node[2])
                self.code.append(f"{target} = {expr}")

            elif node_type == "assign_op":
                target = node[1]
                op = node[2]
                expr = self.generate_code(node[3])
                self.code.append(f"{target} {op} {expr}")

            elif node_type in {"+", "-", "*", "/"}:
                left = self.generate_code(node[1])
                right = self.generate_code(node[2])
                temp = self.new_temp()
                self.code.append(f"{temp} = {left} {node_type} {right}")

            elif node_type == "comparison":
                left = self.generate_code(node[2])
                right = self.generate_code(node[3])
                temp = self.new_temp()

                if node[1] == "EQUAL":
                    self.code.append(f"{temp} = {left} == {right}")
                elif node[1] == "NOTEQUAL":
                    self.code.append(f"{temp} = {left} != {right}")
                elif node[1] == "LESS":
                    self.code.append(f"{temp} = {left} < {right}")
                elif node[1] == "MORE":
                    self.code.append(f"{temp} = {left} > {right}")

                return temp

            elif node_type == "number-expression":
                return str(node[1])

            elif node_type == "id":
                return node[1]

            elif node_type == "do_while":
                start_label = self.new_temp()
                end_label = self.new_temp()

                self.code.append(f"{start_label}:")

                self.generate_block_code(node[1])

                condition = self.generate_code(node[2])

                self.code.append(f"if {condition} goto {start_label}")

                self.code.append(f"goto {end_label}")

                self.code.append(f"{end_label}: ")

            elif node_type == "if":
                condition = self.generate_code(node[1])
                end_label = self.new_label()
                self.code.append(f"if {condition} goto L1")
                self.generate_block_code(node[2])
                self.code.append(f"goto {end_label}")
                self.code.append(f"L1:")
                self.code.append(f"{end_label}")

            elif node_type == "if_elif":
                condition = self.generate_code(node[1])
                end_label = self.new_label()
                elif_label = self.new_label()

                self.code.append(f"if {condition} goto L1")
                self.code.append(f"goto {end_label}")

                self.code.append(f"L1:")
                self.generate_block_code(node[2])
                self.code.append(f"goto {end_label}")

                self.code.append(f"{elif_label}")
                self.code.append(f"if {condition} goto L2")
                self.generate_block_code(node[3])

                self.code.append(f"{end_label}")

            elif node_type == "if_else":
                condition = self.generate_code(node[1])
                end_label = self.new_label()

                self.code.append(f"if {condition} goto L1")
                self.generate_block_code(node[2])
                self.code.append(f"goto {end_label}")
                self.code.append(f"L1:")
                self.generate_block_code(node[3])
                self.code.append(f"{end_label}:")

            elif node_type == "if_elif_else":
                condition = self.generate_code(node[1])
                end_label = self.new_label()
                elif_label = self.new_label()
                else_label = self.new_label()

                self.code.append(f"if {condition} goto L1")
                self.code.append(f"goto {elif_label}")

                self.code.append(f"L1:")
                self.generate_block_code(node[2])
                self.code.append(f"goto {end_label}")

                self.code.append(f"{elif_label}:")
                self.code.append(f"if {condition} goto L2")
                self.generate_block_code(node[3])
                self.code.append(f"goto {else_label}")

                self.code.append(f"{else_label}:")
                self.generate_block_code(node[4])
                self.code.append(f"{end_label}:")

            elif node_type == "print":
                if isinstance(node[1], list):
                    expressions = " ,".join(
                        [str(self.generate_code(expr)) for expr in node[1]]
                    )

                else:
                    expressions = str(self.generate_code(node[1]))

                self.code.append(f"print({expressions})")

    def generate_block_code(self, block):
        for statement in block:
            self.generate_code(statement)

    def get_code(self):
        return "\n".join(self.code)

    def generate_code_output(self):
        with open("code_result.txt", "w") as f:
            f.write(self.get_code())


if __name__ == "__main__":
    generator = CodeGenerator()
    parser = Parser()
    parser.build(debug=True)
    data = """  x = 10; 
                y= 1;
                do { 
                    x -= 1;
                } while ( x > 1 );
                if (x != y || x == y) {
                    print( x ); 
                } elif (x == y && x != y) {
                    print( y ); 
                } else {
                    print( x , y );
                }
            """
    ast = parser.test(data)
    generator.generate_code(ast)
    generator.generate_code_output()
    print(generator.get_code())
