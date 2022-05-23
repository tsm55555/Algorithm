#include <bits/stdc++.h>

using namespace std;

struct Node{
    int data;
    Node* left;
    Node* right;
    Node(int data) : data(data), left(NULL), right(NULL) {}
};

void free_tree(Node*);
bool all_has_value(Node*);
void print_tree(Node*);

int main() {
    string str;
    Node* tree = NULL;
    bool is_complete = true;
    int cases;
    cin >> cases;
    while(cases--) {
        while(cin >> str) {
            if (str == "()") {
                if (is_complete && all_has_value(tree))
                    print_tree(tree);
                else
                    cout << "not complete" << endl;
                free_tree(tree);
                tree = NULL;
                is_complete = true;
                continue;
            }
            if (is_complete == false)
                continue;
            int data = 0;
            int i;
            for (i = 1; str[i] !=  ','; ++i) {
                data = data * 10 + str[i] - '0';
            }
            if (tree == NULL)
                tree = new Node(-1);
            Node* current = tree;
            for (++i; str[i] != ')'; ++i) {
                if (str[i] == 'L') {
                    if (current -> left == NULL)
                        current -> left = new Node(-1);
                    current = current -> left;
                }
                else if (str[i] == 'R') {
                    if (current -> right == NULL)
                        current -> right = new Node(-1);
                    current = current -> right;
                }
            }
            if (current -> data != -1) {
                is_complete = false;
                continue;
            }
            current -> data = data;
        }
    }
}

void free_tree(Node* root) {
    if (root == NULL)
        return;
    free_tree(root -> left);
    free_tree(root -> right);
    free(root);
}

bool all_has_value(Node* root) {
    if (root == NULL)
        return true;
    if (root -> data == -1)
        return false;
    bool has_value;
    has_value = all_has_value(root -> left) && all_has_value(root -> right);
    return has_value;
}

void print_tree(Node* root) {
    vector<Node*> vec;
    vec.push_back(root);
    bool is_print = false;
    while(vec.empty() == false) {
        if (is_print)
            cout << " ";
        Node* current = vec[0];
        vec.erase(vec.begin());
        cout << current -> data;
        if (current -> left != NULL)
            vec.push_back(current -> left);
        if (current -> right != NULL)
            vec.push_back(current -> right);
        is_print = true;
    }
    cout << endl;
}