class Solution(object):
    def fullJustify(self, words, maxWidth):
        res = []
        i = 0
        n = len(words)

        while i < n:
            line = [words[i]]
            line_len = len(words[i])
            i += 1

            while i < n and line_len + 1 + len(words[i]) <= maxWidth:
                line.append(words[i])
                line_len += 1 + len(words[i])
                i += 1

            if i == n or len(line) == 1:
                cur_line = " ".join(line)
                cur_line += " " * (maxWidth - len(cur_line))
            else:
                total_letters = sum(len(w) for w in line)
                total_spaces = maxWidth - total_letters
                gaps = len(line) - 1
                base_space = total_spaces // gaps
                extra = total_spaces % gaps

                cur_line = ""
                for j in range(gaps):
                    cur_line += line[j]
                    cur_line += " " * (base_space + (1 if j < extra else 0))
                cur_line += line[-1]

            res.append(cur_line)

        return res